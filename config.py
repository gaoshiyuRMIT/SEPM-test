import os

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'oracle+cx_oracle://admin:diary-sepm@diary.cghkzjoaxyc8.ap-southeast-2.rds.amazonaws.com/ORCL';
    SQLALCHEMY_TRACK_MODIFICATIONS = False
