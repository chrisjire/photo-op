# from . import main
# from flask_wtf import FlaskForm
# from wtforms import SubmitField,TextAreaField,StringField
# from wtforms.validators import Required,DataRequired,Length,Email


# class updateForm(FlaskForm):
#   bio = TextAreaField('Enter your bio',validators=[Required()])
#   submit = SubmitField('submit')

# class postblog(FlaskForm):
#   category = StringField('Enter a catogory', validators=[Required()])
#   title = StringField('Enter your title', validators=[Required()])
#   post = TextAreaField('Enter your ', validators=[Required()])
#   submit = SubmitField('submit')
  
  

# class UpdateForm(FlaskForm):
#     username = StringField('Username',validators=[DataRequired(),Length(min=3 , max=20)])
#     email = StringField('Email',validators=[DataRequired(),Email()])
#     sumbit = SubmitField('Update')
    
#     def validate_username(self,username):
#         if username.data != current_user.username:
        
#             user = User.query.filter_by(username=username.data).first()
#             if user:
#                 raise ValidationError('already taken. ')
#     def validate_email(self,email):
#         if email.data != current_user.email:
        
#             user = User.query.filter_by(email=email.data).first()
#             if user:
#                 raise ValidationError('already taken. ')
            
# class BlognewForm(FlaskForm):
#     title = StringField('Title',validators=[DataRequired()])
#     detail = TextAreaField('Content',validators=[DataRequired()])
    
    
#     submit = SubmitField('Post')