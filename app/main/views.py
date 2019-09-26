from flask import render_template, request, redirect,flash, url_for, abort  
from . import main  
from ..models import User, Comment , Blog
from flask_login import login_required, current_user
from .. import db, photos
import datetime


@main.route('/')
def index():
    
    '''
    View root page function that returns the index page and its q
    '''
    title = 'Home - Welcome to The best Blog Website Online'
    
    return render_template('index.html', title = title)

