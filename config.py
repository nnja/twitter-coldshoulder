import os

DEBUG = os.getenv('DEBUG', True)

BASEDIR = os.path.abspath(os.path.dirname(__file__))

BOOTSTRAP_USE_MINIFIED = True
BOOTSTRAP_USE_CDN = FalseBOOTSTRAP_FONTAWESOME = True
SECRET_KEY = os.getenv('SECRET_KEY', 'devkey')

