from flask import Flask, request, render_template, jsonify, url_for
from weblablib import WebLab, requires_active, requires_login, weblab_user

# sudo service redis-server start
# set FLASK_APP=laboratory.py
# set FLASK_DEBUG=1
# flask run
# flask weblab fake new
# flask weblab fake new --name "Homer Simpson" --username hsimpson --username-unique "hsimpson@labsland" --assigned-time 60 --back https://en.wikipedia.org/wiki/Homer_Simpson --locale es
app = Flask(__name__)
weblab = WebLab()

app.config.update({
    'SECRET_KEY': 'something-random',
    'WEBLAB_USERNAME': 'weblabdeusto',
    'WEBLAB_PASSWORD': 'password',
})
weblab.init_app(app)

@weblab.initial_url
def initial_url():
    return url_for('index')

@app.route('/')
@requires_login
def index():
    return render_template("lab.html")

@app.route('/status')
@requires_active
def status():
    return jsonify(lights=get_light_status(),
                   time_left=weblab_user.time_left,
                   error=False)
@app.route('/lights/<number>/')
@requires_active
def light(number):
    # request.args is a dictionary with the
    # query arguments (e.g., this checks ?state=true)
    state = request.args.get('state') == 'true'
    # We call the hardware with the state
    hardware.switch_light(number, state)
    # And return the whole status of everything
    return jsonify(lights=get_light_status(), error=False)

def get_light_status():
    lights = {}
    for light in range(1, 11):
        lights['light-{}'.format(light)] = hardware.is_light_on(light)
    return lights

import hardware

@app.cli.command('clean-resources')
def clean_resources_command():
    hardware.clean_resources()
