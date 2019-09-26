from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from . import db, login_manager



@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    bio = db.Column(db.String(255),nullable=Fasle)
    password_hash = db.Column(db.String(255))
    pass_secure= db.Column(db.String(255))

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @property
    def password(self):
        raise AttributeError('You cannot read the password')

    @password.setter
    def password(self,password):
        self.pass_secure= generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'

class Comment(db.Model):
    __tablename__="comment_user"
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(255),nullable = False)
    detail = db.Column(db.String(255),nullable = False)
    date_posted = db.Column(db.DateTime,nullable = False,default = datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False)
    comment = db.relationship('Comment',backref = 'comment_users',lazy="dynamic")


class Photographer(db.Model):
    __tablename__="photo_user"
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(255),nullable = False)
    data_posted = db.Column((db.DateTime,nullable=False,default=datetime.utcnow))
    
  


