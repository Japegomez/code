import uuid
from flask import Blueprint, Response, url_for, render_template, jsonify, session, current_app, request
from flask_cors import cross_origin
from flask_socketio import emit
from mylab import weblab
from mylab.hardware import capture_image, configure_lab, get_measurements
from weblablib import requires_active, requires_login, socket_requires_active, weblab_user, logout
from mylab.api.models import Session, User
from mylab.api.schemas import ImageSchema, MeasurementSchema, SessionSchema

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

    return None

@main_blueprint.route('/api/v1/config', methods=['GET'])
@requires_login
def config():
    user = User(id=uuid.uuid4(), name=weblab_user.username, isActive=weblab_user.active)
    session = Session(id=uuid.uuid4(), assigned_time=weblab_user.time_left, user=user)
    return SessionSchema(include_data=("user",)).dump(session)


@main_blueprint.route('/api/v1/lab', methods=['POST'])
@requires_active
def configureLab():
    data = request.get_json()

    caso = data.get('caso')
    numero = data.get('numero')

    if not caso or not isinstance(numero, int):
        return jsonify(error=True, message="Invalid input data"), 400

    if len(weblab.running_tasks):
        return jsonify(error=True, message="Other tasks being run")

    task = configure_lab.delay(caso, numero)
    print(task.status)

    measurements = get_measurements(caso, numero)

    return MeasurementSchema().dump(measurements)
    

@main_blueprint.route('/api/v1/image', methods=['GET'])
@requires_active
def get_image():
    image = capture_image()
    if image:
        return Response(image, mimetype='image/jpeg')
    return jsonify({'error': 'Failed to capture image'}), 500


@main_blueprint.route('/api/v1/logout', methods=['POST'])
@requires_login
def logout_view():

    if weblab_user.active:
        logout()

    return jsonify(error=False)

