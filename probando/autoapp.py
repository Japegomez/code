import os
from mylab import create_app
# set FLASK_DEBUG=1 # If developing
# set FLASK_APP=autoapp.py
# python run_debug.py if FlaskSocketIO is installed

# flask weblab loop

# flask weblab fake new
if os.environ.get('FLASK_DEBUG') == '1':
    config_name = 'development'
else:
    config_name = os.environ.get('FLASK_CONFIG') or 'default'

app = create_app(config_name)

