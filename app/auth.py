from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, login_user, logout_user, current_user
import re
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

find_email = re.compile(r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)")
auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if loginVerified(email, password):
            user = User.query.filter_by(email=email).first()
            if user and check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for("views.home"))
            else:
                flash('Check email and password and try again', category='error')

    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        phone = request.form.get('phone')
        email = request.form.get('email')
        password = request.form.get('password')
        passwordConfirm = request.form.get('passwordConfirm')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Account exists with that email', category='error')
        elif signupVerified(fname, lname, phone, email, password, passwordConfirm):
            new_user = User(fname=fname, lname=lname, phone=phone, email=email, password=generate_password_hash(password, method='sha256'))

            try:
                db.session.add(new_user)
                db.session.commit()
            except:
                db.session.rollback()

            login_user(user, remember=True)
            return redirect(url_for('auth.login'))

    return render_template("signup.html", user=current_user)

def loginVerified(email, password):
    try:
        email = find_email.findall(email)[0]
    except:
        email = email
    if len(email) > 4 and len(password) > 7:
        return True

    elif len(email) < 4:
        flash('Invalid Email', category='error')
    elif len(password) < 7:
        flash('Password too short', 'error')
    return False

def signupVerified(fname, lname, phone, email, password, passwordConfirm):
    try:
        email = find_email.findall(email)[0]
    except:
        email = email
    if len(fname) > 2 and len(email) > 4 and passwordConfirm == password and len(password) > 7:
        flash('Account created', category='success')
        return True

    if len(fname) < 2:
        flash('Firstname must be at least 2 characters', category='error')
    elif len(email) < 4:
        flash('Invalid Email', category='error')
    elif len(password) < 7:
        flash('Password too short (at least 7 characters)', 'error')
    elif password != passwordConfirm:
        flash('Passwords do not match', 'error')

    return False