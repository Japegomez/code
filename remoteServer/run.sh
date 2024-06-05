#!/bin/sh
# sudo service redis-server start only if not running
if [ -z "$(pgrep redis-server)" ]; then
    sudo service redis-server start
fi
export FLASK_DEBUG=1
export FLASK_APP=autoapp.py
export SECRET_KEY='cM68vny57y1XlOsXEC1q'
python run_debug.py