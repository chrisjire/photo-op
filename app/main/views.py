
from flask import render_template, request, redirect,flash, url_for, abort  
from . import main  
from ..models import User,Post,Comment
from .. import db, photos
from .forms import PostForm,CommentForm,UpdateProfile
from flask_login import login_required,current_user
import datetime
import json 
import urllib.request,json


@main.route('/')
def index():
    
    '''
    View root page function that returns the index page and its q
    '''
    title = 'Home - Welcome to The best Post Website Online'
    
    return render_template('index.html', title = title)

@main.route('/cam')
def cameraman():
    
    '''
    View root page function that returns the index page and its q
    '''
    
    return render_template('Cameraman.html')


@main.route('/cameraman1')
def cameraman1():
    return render_template('Cameraman-1.html')
@main.route('/cameraman2')
def cameraman2():
    return render_template('Cameraman-2.html') 
@main.route('/cameraman3')
def cameraman3():
    return render_template('Cameraman-3.html') 
@main.route('/cameraman4')
def cameraman4():
    return render_template('Cameraman-4.html') 
@main.route('/cameraman5')
def cameraman5():
    return render_template('Cameraman-5.html') 
@main.route('/cameraman6')
def cameraman6():
    return render_template('Cameraman-6.html')    

@main.route('/user/<uname>/up-pic', methods=['GET', 'POST'])
@login_required
def updates_pic():
    user = User.query.all()
    '''
    View root page function that returns the index page and its q
    '''
    
    return render_template('profile/pic.html', user=user)




@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    user_joined = user.date_joined.strftime('%b %d, %Y')

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user,date = user_joined)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    
    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)


@main.route('/user/<uname>/update/pic', methods=['GET','POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()

    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()

    return redirect(url_for('main.profile',uname=uname))

@main.route('/post/new', methods = ['GET','POST'])
@login_required
def new_post():
    post_form = PostForm()
    if post_form.validate_on_submit():
        title = post_form.title.data
        text = post_form.text.data
        

        # Updated post instance
        new_post = Post(title=title,text=text)

        # Save post method
        new_post.save_post()
        return redirect(url_for('.index'))

    title = 'New post'
    return render_template('new_post.html',title = title,post_form=post_form )

@main.route('/posts')
def all_posts():
    posts = Post.query.order_by(Post.date_posted.desc()).all()

    title = 'photo posts'

    return render_template('posts.html', title = title, posts = posts)

@main.route('/post/<int:id>',methods=['GET','POST'])
def post(id):

    form = CommentForm()
    post = Post.get_post(id)

    if form.validate_on_submit():
        comment = form.text.data

        new_comment = Comment(comment = comment,user = current_user,post = post.id)

        new_comment.save_comment()


    comments = Comment.get_comments(post)

    title = f'{post.title}'
    return render_template('post.html',title = title, post = post, form = form, comments = comments)

@main.route('/delete_comment/<id>/<post_id>',methods = ['GET','POST'])
def delete_comment(id,post_id):
    comment = Comment.query.filter_by(id = id).first()

    db.session.delete(comment)
    db.session.commit()

    return redirect(url_for('main.post',id = post_id))

@main.route('/delete_post/<id>',methods = ['GET','POST'])
def delete_post(id):
    post = Post.query.filter_by(id = id).first()

    db.session.delete(post)
    db.session.commit()

    return redirect(url_for('main.all_posts'))

@main.route('/subscribe/<id>')
def subscribe(id):
    user = User.query.filter_by(id = id).first()

    user.subscription = True

    db.session.commit()

    return redirect(url_for('main.index'))

@main.route('/post/update/<id>',methods = ['GET','POST'])
def update_post(id):
    form = PostForm()

    post = Post.query.filter_by(id = id).first()

    form.title.data = post.title
    form.text.data = post.text

    if form.validate_on_submit():
        title = form.title.data
        text = form.text.data

        post.title = title
        post.text = text

        db.session.commit()

        return redirect(url_for('main.post',id = post.id))

    return render_template('update.html',form = form)

@main.route('/user/<uname>/photos')
def user_photos(uname):
    user = User.query.filter_by(username=uname).first()
    photos = Post.query.filter_by(user_id = user.id).all()
    # photos_count = photo.count_photos(uname)
    user_joined = user.date_joined.strftime('%b %d, %Y')

    return render_template("profile/photos.html", user=user, posts=photos,date = user_joined)
>>>>>>> origin/Dev
