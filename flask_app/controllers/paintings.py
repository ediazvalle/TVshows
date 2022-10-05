from flask_app import app
from flask import Flask, render_template, redirect, flash, session, request
from flask_app.models.painting import Painting
from flask_app.models.user import User

@app.route('/dashboard/')
def dashboard():
    if 'user_id' not in session:
        flash("MUst log in")
        return redirect('/')
    data = {
        'id': session['user_id']
    }
    theUser = User.getOne(data)
    userpaintings = Painting.allEntries()
    return render_template('dashboard.html', user=theUser, paintings=userpaintings)


@app.route('/newpainting')
def newpainting(): 
    if 'user_id' not in session:
        flash('Must log in')
        return redirect('/')
    data = {
        'id': session['user_id']
    }
    theUser = User.getId(data)
    return render_template('newPainting.html', user=theUser)


@app.route('/addpainting/', methods=['POST'])
def newpainting():
    data = {
        'title': request.form['title'],
        'description': request.form['description'],
        'price': request.form['price'],
        'user_id': session['user_id']
        }
    Painting.save(data)
    flash("Youre painting has been saved")
    return redirect('/dashboard/')

@app.route('/<int:painting_id/delete/')
def deletePainting(painting_id):
    data = {
        'id': painting_id
    }
    Painting.delete(data)
    flash('Painting has been deleted')
    return redirect('/dashboard/')

@app.route('/int:painting_id>/display/')
def displayPainting(painting_id):
    if 'user_id' not in session:
        flash('Must log in')
        return redirect('/')
    data = {
        'id': session['user_id']
    }
    paintingData = {
        'id': painting_id
        }
    theUser = User.getId(data)
    theUsers = User.getAll()
    thePainting = Painting.getId(paintingData)
    return render_template('displaypainting.html', user=theUser,users=theUsers,paintings=thePainting)

@app.route('/<int:painting_id>/edit/')
def editPainting(painting_id):
    if 'user_id' not in session:
        flash('Must log in')
        return redirect('/')
    data = {
        'id': session['user_id']
    }
    paintingData = {
        'id': painting_id
        }
    theUser = User.getId(data)
    thePainting = Painting.getId(paintingData)
    return render_template('editpainting.html', user=theUser,painting=thePainting)

@app.route('/<int:painting_id/update/', methods=['POST'])
def updatePainting(painting_id):
        data = {
        'id': 'painting_id',
        'title': request.form['title'],
        'description': request.form['description'],
        'price': request.form['price'],
        }
        Painting.update(data)
        flash('Painting has been updated')
        return redirect('/dashboard/')