from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.books import Books
from flask_app.models.authors import Authors

# home page
@app.route('/')
def home():
    all_users = Authors.show_all_users()
    return render_template('home.html',all_users=all_users)

# add user
@app.route('/create',methods=['POST'])
def create_user():
    data={
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name']
    }
    Authors.add_users(data)
    return redirect('/')

# authors page
@app.route('/authors/<int:id>')
def authors(id):
    data={
        'id':id
    }
    one_user=Authors.get_one(data)
    one_book=Authors.get_user_favorites(data)
    all_books=Books.show_all_books(data)
    
    return render_template('authors.html',one_book=one_book,one_user=one_user,all_books=all_books)


@app.route('/create/<int:id>', methods=['POST'])
def add_favorite(id):
    data={
        'id':id,
        'book_id':int(request.form['book_id'])
    }
    add_fav=Books.add_book_to_favorites(data)
    return redirect(f'/authors/{id}')


@app.route('/book')
def show_book():

    all_books=Books.show_all_books()
    
    return render_template("books.html",all_books=all_books)



@app.route('/book/create',methods=['POST'])
def add_book():
    data={
        "title":request.form['title'],
        "num_of_pages":request.form['num_of_pages']
    }
    Books.add_book(data)
    return redirect('/book')