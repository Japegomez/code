import os
from mylab import create_app
# sudo service redis-server start
# export FLASK_DEBUG=1 # If developing
# export FLASK_APP=autoapp.py
# python3.9 run_debug.py if FlaskSocketIO is installed

# flask weblab loop

# flask weblab fake new
if os.environ.get('FLASK_DEBUG') == '1':
    config_name = 'development'
else:
    config_name = os.environ.get('FLASK_CONFIG') or 'default'

app = create_app(config_name)

