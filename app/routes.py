from app import app, db
from app.forms import LoginForm, RegistrationForm
from flask import render_template, redirect, flash, url_for
from flask_login import current_user, login_user, logout_user

from app.models import Post, User, Plans

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Brian'}
    posts = Post.query.all()
    return render_template('index.html', user=user, posts = posts, title='A title')

@app.route('/club')
def club():
    plans = Plans.query.all()
    return render_template('club.html', plans = plans)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():  # post and submit validate
        # get the user from data base use code
        user = User.query.filter_by(username=form.username.data).first()
        flash('Hello, {}!'.format(form.username.data))

        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))

        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))

    return render_template('login.html', title = 'Sign In', form = form) # GET or submit validate Failed

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods = ['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)

        db.session.add(user)
        db.session.commit()

        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title = 'Register', form = form)