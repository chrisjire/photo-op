from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from . import db, login_manager


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    
    password_hash = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))

    @property
    def password(self):
         AttributeError('You cannot read the password')

    @password.setter
    def password(self,password):
        self.password= generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password,password)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)
    
    def __repr__(self):
        return f'User {self.username}'



@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)
