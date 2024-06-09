import os


class Config(object):
    DEBUG = False
    DEVELOPMENT = False
    TESTING = False

    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(32)

    WEBLAB_USERNAME = os.environ.get('WEBLAB_USERNAME') or 'weblabdeusto'
    WEBLAB_PASSWORD = os.environ.get('WEBLAB_PASSWORD') or 'password'

    # If an unauthorized user comes in, redirect him to this link
    # WEBLAB_UNAUTHORIZED_LINK = 'https://google.es/'

    # Alternatively, you can establish a template that will be rendered
    #WEBLAB_UNAUTHORIZED_TEMPLATE = 'unauthorized.html'

    # These URLs should change to customize your lab:
    SESSION_COOKIE_NAME = 'complete-session'
    SESSION_COOKIE_PATH = '/'
    WEBLAB_SESSION_ID_NAME = 'wl-mylab'
    WEBLAB_REDIS_BASE = 'mylab-complete'
    SERVER_NAME = 'pi:5000'
    
    # If you put this, for example, then you should configure
    # WebLab-Deusto to use http://<lab-server>/deusto/weblab/
    WEBLAB_BASE_URL = '/deusto'

    WEBLAB_NO_THREAD = False

    # Other parameters (and default values):
    #
    WEBLAB_TIMEOUT = 300 # If the user doesn't reply in 5 minutes, consider expired
    WEBLAB_REDIS_URL = 'redis://localhost:6379/0'
    WEBLAB_TASK_EXPIRES = 100 # Time to expire the session results
    WEBLAB_EXPIRED_USERS_TIMEOUT = 0 # How long an expired user can be before kicked out
    # WEBLAB_AUTOPOLL = True # Every method calls poll()



class DevelopmentConfig(Config):
    DEBUG = True
    DEVELOPMENT = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'shared_secret_key'
    ASSETS_DEBUG = True


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    # WEBLAB_SCHEME = 'https'
    pass


config = {
    'default': ProductionConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}
