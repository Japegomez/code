import time

from flask import Blueprint, url_for, render_template, jsonify, session, current_app, request
from flask_cors import cross_origin
from flask_socketio import emit
import weblablib

from mylab import weblab, socketio
from mylab.client import client_status, switch_light
from mylab.hardware import program_device, hardware_status

from weblablib import requires_active, requires_login, socket_requires_active, weblab_user, logout

from mylab.templates.api.models import Session, User
from mylab.templates.api.schemas import SessionSchema

main_blueprint = Blueprint('main', __name__)


@weblab.initial_url
def initial_url():
    """
    Where do we send the user when a new user comes?
    """
    return "http://pi:4200"

@main_blueprint.route('/')
@requires_login
def index():
    # This method generates a random identifier and stores it in Flask's session object
    # For any request coming from the client, we'll check it. This way, we avoid
    # CSRF attacks (check https://en.wikipedia.org/wiki/Cross-site_request_forgery )
    session['csrf'] = weblab.create_token()

    return render_template("index.html")

@main_blueprint.route('/api/v1/config', methods=['GET'])
@requires_login
def config():
    user = User(id="1", name=weblab_user.username, isActive=weblab_user.active)
    session = Session(id="1", assigned_time=weblab_user.time_left, user=user)
    return SessionSchema(include_data=("user",)).dump(session)


@main_blueprint.route('/api/v1/lab/')
@requires_active
def lab():
    return jsonify('ok')
###################################################################
#
#
# Socket-IO management
#

@socketio.on('connect', namespace='/mylab')
@socket_requires_active
def connect_handler():
    emit('update-client', client_status(), namespace='/mylab')

@socketio.on('lights', namespace='/mylab')
@socket_requires_active
def lights_event(data):
    state = data['state']
    number = data['number']
    switch_light(number, state)
    emit('update-client', client_status(), namespace='/mylab')

@socketio.on('program', namespace='/mylab')
@socket_requires_active
def microcontroller():
    
    # If there are running tasks, don't let them send the program
    if len(weblab.running_tasks):
        return jsonify(error=True, message="Other tasks being run")

    task = program_device.delay()

    # Playing with a task:
    current_app.logger.debug("New task! {}".format(task.task_id))
    current_app.logger.debug(" - Name: {}".format(task.name))
    current_app.logger.debug(" - Status: {}".format(task.status))

    # Result and error will be None unless status is 'done' or 'failed'
    current_app.logger.debug(" - Result: {}".format(task.result))
    current_app.logger.debug(" - Error: {}".format(task.error))

@main_blueprint.route('/logout', methods=['POST'])
@requires_login
def logout_view():
    if not _check_csrf():
        return jsonify(error=True, message="Invalid JSON")

    if weblab_user.active:
        logout()

    return jsonify(error=False)

#######################################################
#
#   Other functions
#


def _check_csrf():
    expected = session.get('csrf')
    if not expected:
        current_app.logger.warning(
            "No CSRF in session. Calling method before loading index?")
        return False

    obtained = request.values.get('csrf')
    if not obtained:
        # No CSRF passed.
        current_app.logger.warning("Missing CSRF in provided data")
        return False

    return expected == obtained
