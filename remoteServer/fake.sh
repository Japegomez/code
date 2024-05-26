#!/bin/sh
export FLASK_DEBUG=1
export FLASK_APP=autoapp.py
flask weblab fake new --assigned-time $1 --username $2