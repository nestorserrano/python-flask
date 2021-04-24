from flask import Flask, render_template, jsonify, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://jseldllnjyvung:7ec2dd9c0cb6e1b3e8246e7ea9debf108c2c76c0927b8a48c98d7d9808d9875e@ec2-3-222-127-167.compute-1.amazonaws.com:5432/d8fqv4s9r7c82d'

db = SQLAlchemy(app)

class Nomina(db.Model):
  __tablename__ = "nomina"

  cedula = db.Column(db.Integer, primary_key=True)
  fullname = db.Column(db.String(50), nullable = False)
  sueldobas = db.Column(db.float), nullable = True)
  bono = db.Column(db.Float), nullable = True)


  def __init__(self,cedula,fullname,sueldobas,bono):
    self.cedula = cedula
    self.fullname = fullname
    self.sueldobas = dueldobas
    self.bono = bono

@app.route("/")
def index():
    return "Hello Nestor"
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM nomina')
    data = cur.fetchall()
    return render_template('index.html', nominas = data)

