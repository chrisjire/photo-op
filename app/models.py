from . import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from datetime import datetime


class User(UserMixin,db.model):
    __tablename__="users"
    
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(255),unique = True , nullable = False)
    email = db.Column(db.String(255),unique = True, nullable = False)
    passwod = db.Column(db.String(255),nullable = False)
    comment = db.relationship
    
    def save(self):
      db.session.add(self)
      db.session.commit()

    def delete(self):
      db.session.delete(self)
      db.session.commit()

    def __repr__(self):
      return f'User {self.username}'
    