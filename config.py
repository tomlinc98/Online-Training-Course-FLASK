import os, secrets

# define base directory of app
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	# key for CSF
	SECRET_KEY = os.environ.get('SECRET_KEY') or secrets.token_hex(32)
	# sqlalchemy .db location (for sqlite)
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
	# sqlalchemy track modifications in sqlalchemy
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	MAIL_SERVER = os.environ.get('MAIL_SERVER')
	MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
	MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
	MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
	MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
	ADMINS = ['email@email.com']
	# enable fontawesome
	BOOTSTRAP_FONTAWESOME = True
	BOOTSTRAP_USE_CDN = True # not working? just download the cdn and link to it in static/js/
	BOOTSTRAP_JQUERY_VERSION = '3.2.1'
	BOOTSTRAP_SERVE_LOCAL = False