import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DB_URI = os.environ.get('DB_URI')
    
