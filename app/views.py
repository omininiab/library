from flask import Blueprint, render_template, request, flash, jsonify, redirect
from flask_login import login_required, current_user
from .models import Book
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@views.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        nPages = request.form.get('nPages')
        pagesRead = request.form.get('pagesRead')

        if bookVerified(title, author, nPages, pagesRead):
            new_book = Book(title=title[:150].title(), author=author[:150].title(), nPages=int(nPages), pagesRead=int(pagesRead), userid=current_user.id)
            try:
                db.session.add(new_book)
                db.session.commit()
                flash('Book added!', category='success')
                return redirect(request.url)
            except:
                db.session.rollback()
                flash('Error occurred while attempting to add book', category='error')

    return render_template("home.html", user=current_user)

@views.route('/delete-book', methods=['POST'])
@login_required
def delete_book():
    book = json.loads(request.data)
    bookID = book['bookID']
    book = Book.query.get(bookID)
    if book:
        if book.userid == current_user.id:
            try:
                db.session.delete(book)
                db.session.commit()
                flash('Book deleted', category='success')

            except:
                db.session.rollback()
                flash('Error occurred while attempting to delete book', category='error')

    return jsonify({})

def bookVerified(title, author, nPages, pagesRead):
    if len(title) > 0 and len(author) > 0 and int(nPages)>0 and int(pagesRead)>=0 and int(pagesRead) <= int(nPages):
        return True
    flash('Error occurred while attempting to add book', category='error')

    return False