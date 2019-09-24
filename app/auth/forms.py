from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,TextAreaField
from wtforms.validators import Required,Email,EqualTo,ValidationError
from ..models import User

class RegitrationForm(FlaskForm):
    username = StringField('Enter Email Address', validators=[Required(),Email()])
    email = StringField('Enter your username',validators=[Required(),Email()])
    password = PasswordField('Enter a password: ',validators=[Required(),EqualTo('password_confirm',message='passwords must match')])
    Submit = SubmitField('sign up')
    
    def validate_email(self,data_field):
        if User.query.filter_by(email = data_field.data).first():
            
    
    