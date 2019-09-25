from .import auth
from flask import render_template,request,redirect,url_for,flash
from app.models import User
from flask_login import login_user,logout_user

@auth.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        form = request.form
        username = form.get('username')
        password = form.get('password')
        user = User.query.filter_by(username = username).first()
        if user != None:
            if user.check_password(password) != False:
                flash("Succesfully logged in",'success')
                login_user(user)
                return redirect(url_for('main.index'))
            
            else:
                flash("Invalid Password","login")
                return render_template('auth/login.html',username=username)
        else:
                flash("Invalid Username","login")
                return render_template('auth/login.html')
    return render_template('auth/login.html')

@auth.route('/signup',methods=['POST','GET'])
def signup():
    if request.method == "POST":
        form = request.form
        username = form.get('username')
        email = form.get('email')
        password =form.get('password')
        confirm_password = form.get('confirm_password')
        if password != confirm_password:
            flash("passwords dont match","password")
            return render_template('auth/signup.html',email=email, username = username)
        user = User.query.filter_by(username = username).first()
        else:
            flash("Username is already taken","username")
            return render_template('auth/signup.html',email = email, password = password, confirm_password = confirm_password)
    return render_template('auth/signup.html')

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))