import os

class Config:
    SECRET_KEY = "os.urandom(24)"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://medinsight_user:your_password@localhost/medinsight_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False