import os

class Config:
    DEBUG=True
    SECRET_KEY = '1234g5'
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://hidri:1234@localhost/photoop'

class ProdConfig(Config):
    DEBUG = False
    