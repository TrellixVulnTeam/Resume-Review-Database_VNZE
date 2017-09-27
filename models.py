from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from app import app

class (db.Model):
  id = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String(20), unique = True)

  def __init__(self,username,id):
    self.username = username
    self.id = id

  def __rep__(self):
    return'<User %r>' % self.username