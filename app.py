from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from views import *;

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Reddit@localhost/postgres'
db = SQLAlchemy(app)

# @app.route('/')
# def home():
#     return "Success";
# class Test(db.Model):
#   id = db.Column(db.Integer, primary_key = True)
#   username = db.Column(db.String(20), unique = True)
#
#   def __init__(self,username,id):
#     self.username = username
#     self.id = id
#
#   def __rep__(self):
#     return'<User %r>' % self.username


if __name__ =="__main__":
    app.run()
    app.debug = True;