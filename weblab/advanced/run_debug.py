from mylab import create_app
import os
from gevent import monkey
monkey.patch_all()


if os.environ.get('FLASK_DEBUG') == '1':
    config_name = 'development'
else:
    config_name = os.environ.get('FLASK_CONFIG') or 'default'

app = create_app(config_name)
app.run(debug=True)
