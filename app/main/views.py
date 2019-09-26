# from . import main
# from flask import redirect,render_template,url_for,request,abort,flash
# from flask_login import login_required,current_user
# from ..models import User
# # from .forms import updateForm,postpics
# # from .. import db,photos
# # from .forms import BlognewForm,UpdateForm



# # @main.route("/")
# @main.route("/index")
# def index():

#   return render_template('index.html')

# @main.route("/user_account", methods=['GET','POST'])
# def user_account():
    
#     form = UpdateForm()
#     if form.validate_on_submit():
#         current_user.username = form.username.data
#         current_user.email = form.email.data
#         db.session.commit()
#         flash('you profile has been updated','success')
#         return redirect(url_for('main.profile'))
    
#     elif request.method == 'GET':
#         form.username.data = current_user.username 
#         form.email.data = current_user.email
          

#     return render_template('profile.html',title='User_account', form=form)

# @main.route("/blog_new",methods=['GET','POST'])

# @login_required
# def photographer_page():
    
#     form = BlognewForm ()
#     if form.validate_on_submit():
#         photographer_page = Photographer (title=form.title.data, detail=form.detail.data,writer_id=current_user.id)
#         db.session.add(photographer_page )
#         db.session.commit()
#         flash('Your post is created !'  , 'success')
#         return redirect (url_for('main.index'))
#     return render_template('photo_page.html',title='photographer_page',form=form)
  