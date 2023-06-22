from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL


class Authors:
    def __init__(self,data):
        self.id =data['id']
        self.first_name =data['first_name']
        self.last_name =data['last_name']
        self.created_at =data['created_at']
        self.updated_at =data['updated_at']
        
        self.users = []

        # add a user
    @classmethod
    def add_users(cls,data):
        query = """
        INSERT INTO 
        users (first_name, last_name)
        VALUES (%(first_name)s, %(last_name)s);
        """
        return connectToMySQL('books_schema').query_db( query, data)
    
    # show one user
    @classmethod
    def get_one(cls,data):
        query = """
        SELECT *
        FROM users
        WHERE id = %(id)s
        """
        user_from_db= connectToMySQL('books_schema').query_db(query,data)
        return cls(user_from_db[0])

    # show all users
    @classmethod
    def show_all_users(cls):
        query = """
        SELECT *
        FROM users
        """
        return connectToMySQL('books_schema').query_db( query)
    
    # get one user data with id using ##LEFTJOIN##
    @classmethod
    def get_user_favorites(cls,data):
        query = """
        SELECT title, num_of_pages
        FROM books
        LEFT JOIN favorites
        ON books.id = favorites.book_id
        LEFT JOIN users
        ON users.id = favorites.user_id
        WHERE users.id=%(id)s
        """
        return connectToMySQL('books_schema').query_db( query,data)
    


