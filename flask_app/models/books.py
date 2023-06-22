from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL

class Books:
    DB = 'books_schema'

    def __init__(self,data):
        self.id =data['id']
        self.title =data['title']
        self.num_of_pages =data['num_of_pages']
        self.created_at =data['created_at']
        self.updated_at =data['updated_at']
        self.books = []


    @classmethod
    def add_book(cls,data):
        query = """
        INSERT INTO 
        books (title, num_of_pages)
        VALUES (%(title)s, %(num_of_pages)s);
        """
        return connectToMySQL('books_schema').query_db( query, data)
    
    @classmethod
    def show_all_books(cls):
        query = """
        SELECT *
        FROM books
        """
        return connectToMySQL('books_schema').query_db( query)
    
    # add book to favorites
    @classmethod
    def add_book_to_favorites(cls,data):
        query="""
        INSERT INTO favorites
        (user_id, book_id) VALUES (%(id)s, %(book_id)s);
        """
        return connectToMySQL('books_schema').query_db( query, data)
    
    @classmethod
    def get_one(cls,data):
        query = """
        SELECT *
        FROM books
        WHERE id = %(id)s
        """
        user_from_db= connectToMySQL('books_schema').query_db(query,data)
        return cls(user_from_db[0])
    

    

    



