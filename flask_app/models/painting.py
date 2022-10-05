from operator import le
from turtle import title

from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL


class Painting:
    db = 'painting_exam'
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['title']
        self.last_name = data['description']
        self.email = data['price']
        self.createdat = data['createdat']
        self.updatedat = data['updatedat']
        self.updatedat = data['user_iduser']

    def paintings(self):
        return self.painting

    @staticmethod
    def validate(painting):
        is_valid = True
        if len(painting['title']) or len(painting['description']) or len(painting['price']) <= 0:
            flash("All fields required")
            is_valid=False
        if len(painting['title']) < 2:
            flash("Title must be longer than 2 characters")
            is_valid=False
        if len(painting['description']) < 10:
            flash("Description must be longer than 1o characters")
            is_valid=False
        if painting['price'] <= 0:
            flash("Price needs to be greater than 0")
            is_valid=False
        return is_valid

    @classmethod
    def getAll(cls,data):
        query = "SELECT * FROM painting;"
        results = connectToMySQL(cls.db_name).query_db(query)
        users = []
        for row in results:
            users.append( cls(row))
        return users

    @classmethod
    def getId(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        return cls(results[0])

    @classmethod
    def save(cls,data):
        query = 'INSERT INTO users (title,description,price,user_iduser) VALUES (%(title),%(description),%(price),%(user_iduser));'
        return connectToMySQL(cls.db_name).query_db(query,data)

    @classmethod
    def update(cls,data):
        query = "UPDATE painting SET title=%(title)s, description=%(description)s, price=%(price)s WHERE id=%(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM painting SET WHERE id=%(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)
    
    @classmethod
    def allpaintings(cls):
        query = 'SELECT * FROM painting JOIN user on painting.user_id = user.id;'
        results = connectToMySQL(cls.db_name).query_db(query)
        print('All paintings: ', results)
        return results
