from ast import Return
from optparse import Values
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    db = 'painting_exam'
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.confirm_password = data['confirm_password']
        self.createdat = data['createdat']
        self.updatedat = data['updatedat']


@staticmethod
def validate(user):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(User.db_name).query_db(query,user)
        if len(results) >= 1:
            flash("Email already taken.")
            is_valid=False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid Email")
            is_valid=False
        if len(user['first_name']) < 3:
            flash("First name must be at least 3 characters")
            is_valid= False
        if len(user['last_name']) < 3:
            flash("Last name must be at least 3 characters")
            is_valid= False
        if len(user['password']) < 8:
            flash("Password must be at least 8 characters")
            is_valid= False
        if user['password'] != user['confirm_password']:
            flash("Passwords don't match")
        return is_valid

@classmethod
def getAll(cls,data):
        query = "SELECT * FROM users;"
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
def getEmail(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])

@classmethod
def save(cls,data):
    query = 'INSERT INTO users (first_name,last_name,email,password) VALUES (%(first_name),%(last_name),%(email),%(password));'
    return connectToMySQL(cls.db_name).query_db(query,data)


