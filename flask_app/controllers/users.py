from flask_app import app
from flask import Flask,render_template,redirect,flash,session,request
from flask_app.models.user import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template(index.html)

@app.route('/register/', methods=['POST'])
def register():
    is_valid = User.validate(request.form)
    if not is_valid:
        return redirect('/')
    newUser = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': bcrypt.generate_password_hash(request.form['first_name'])
    }
    id = User.save(newUser)
    if not id:
        flash("Fill out correctly")
        return redirect('/')
    session['user_id'] = id
    flash('logged in')
    return redirect('/dashboard/')

@app.route('/login/', methods=['POST'])
def login():
    data = {
        'email': request.form['email']
    }
    user = User.getEmail(data)
    if not user:
        flash("INVALID EMAIL OR PASSWORD")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password,request.form['password']):
        flash("INVALID EMAIL OR PASSWORD")
        return redirect('/')
    session['user_id'] = user.id
    flash("Welcome")
    return redirect('/dashboard/')

@app.route('/logout/', methods=['POST'])
def logout():
    session.clear()
    return redirect('/')


