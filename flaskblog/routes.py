from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post

posts = [
    {
        'author':"Author1",
        'title':"Title1",
        'content':"Content1",
        'date_posted' : "20 April 2019"
    },  
    {
        'author':"Author3",
        'title':"Title2",
        'content':"Content2",
        'date_posted' : "21 April 2019"
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts = posts,
        title = "Home")

@app.route('/about')
def about():
    return render_template('about.html', title = "About")

@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title = "Register", form = form)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@admin.com' and form.password.data == 'password':
            flash(f'Sucessfully Logged in', 'success')
            return redirect(url_for ('home'))
        else:
            flash(f'Try Again', 'danger')
    return render_template('login.html', title = "Login", form = form)

