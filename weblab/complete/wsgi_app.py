import logging
from mylab import create_app
import os
import sys
import six

MYLAB_DIR = os.path.abspath(os.path.dirname(__file__))

sys.path.insert(0, MYLAB_DIR)
os.chdir(MYLAB_DIR)

if six.PY2:
    sys.stdout = open('stdout.txt', 'w', 0)
    sys.stderr = open('stderr.txt', 'w', 0)
else:
    sys.stdout = open('stdout.txt', 'w')
    sys.stderr = open('stderr.txt', 'w')

#
# XXX Change these values here XXX
#
# Don't use these values. Run a Python terminal and run:
# >>> import os
# >>> os.urandom(32)
# to get new value.
os.environ['SECRET_KEY'] = '\x1c-\xf8\xd0\xc4\xa8Qtg\xcf"W/5 \xed\xb4sI\xf1\xab\xc9RI\xd4\xfc\xf4\xc3\x1eD\xaeO'
os.environ['WEBLAB_USERNAME'] = 'weblabdeusto'
os.environ['WEBLAB_PASSWORD'] = 'password'

application = create_app('production')

file_handler = logging.FileHandler(filename='errors.log')
file_handler.setLevel(logging.INFO)
application.logger.addHandler(file_handler)
