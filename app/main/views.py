
from flask import render_template, request, redirect,flash, url_for, abort  
from . import main  
from ..models import User,Blog
from flask_login import login_required, current_user
from .forms import UpdateForm,UsernewForm

import datetime

# 
@main.route("/")
@main.route("/index")
def index():
  blogs = Blog.query.all()
  return render_template('index.html', blogs=blogs)


@main.route("/Cameraman", methods=['GET','POST'])
def Cameraman():
    
    form = UpdateForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('you profile has been updated','success')
        return redirect(url_for('main.Cameraman'))
    
    elif request.method == 'GET':
        form.username.data = current_user.username 
        form.email.data = current_user.email
          
    # image_file = url_for('static',filename='images/' + current_user.image_file)
    return render_template('Cameraman.html',title='Cameraman', form=form)

# @main.route("/comment_new",methods=['GET','POST'])

# @login_required
# def comment_new():
    
#     form = UsernewForm()
#     if form.validate_on_submit():
#         comment_new = Post(title=form.title.data, detail=form.detail.data,writer_id=current_user.id)
#         db.session.add(comment_new)
#         db.session.commit()
#         flash('Your post is created !'  , 'success')
#         return redirect (url_for('Cameraman.html'))
#     return render_template('create_post.html',title='comment_new',form=form)


@main.route("/blog_new",methods=['GET','POST'])

@login_required
def blog_new():
    
    form = UsernewForm ()
    if form.validate_on_submit():
        blog_new = Blog(title=form.title.data, detail=form.detail.data,writer_id=current_user.id)
        db.session.add(blog_new)
        db.session.commit()
        flash('Your post is created !'  , 'success')
        return redirect (url_for('main.index'))
    return render_template('create_post.html',title='blog_new',form=form)
  