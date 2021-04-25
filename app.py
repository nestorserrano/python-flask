from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo


app = Flask(__name__)
uri = "postgres://jseldllnjyvung:7ec2dd9c0cb6e1b3e8246e7ea9debf108c2c76c0927b8a48c98d7d9808d9875e@ec2-3-222-127-167.compute-1.amazonaws.com:5432/d8fqv4s9r7c82d"
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'cualquierclave'    

db = SQLAlchemy(app)


class Nomina(db.Model):
    __tablename__ = "nomina"

    cedula = db.Column(db.Integer, primary_key=True, unique = True)
    fullname = db.Column(db.String(50), nullable = False)
    sueldobas = db.Column(db.Float)
    bono = db.Column(db.Float)
    create_at = db.Column(db.DateTime(timezone=True), server_default=func.now())


    def validate_cedula(self, field):
        if Nomina.query.filter_by(cedula=field.data).first():
            raise ValidationError('Cedula is already in use.')


    def __init__(self,cedula,fullname,sueldobas,bono):
        self.cedula = cedula
        self.fullname = fullname
        self.sueldobas = sueldobas
        self.bono = bono

    def __repr__(self):
       return '<Contacto: {}>'.format(self.fullname)

    
    def __str__(self):
        return self.fullname

@app.route("/")
def index():
  data = Nomina.query.all()
  return render_template('index.html', nominas = data)

@app.route('/agregar', methods=['POST'])
def addcontact():
    if request.method == 'POST':
        cedula = request.form['cedula']
        fullname = request.form['fullname']
        sueldobas = request.form['sueldobas'] 
        bono = request.form['bono']
        new_contact = Nomina(cedula=cedula, fullname=fullname,sueldobas=sueldobas,bono=bono)
        db.session.add(new_contact)
        db.session.commit()
        flash('Contacto agregado satisfactoriamente')
        return redirect(url_for('index'))
    elif request.method == 'GET':    
        data = Nomina.query.all()
        results = [
            {
                "cedula": data.cedula,
                "fullname": data.fullname,
                "sueldobas": data.sueldobas,
                "bono": data.bono,
                "create_at": data.create_at

            } for nomina in data]

        return {"count": len(results), "Contactos": results}

@app.route('/edit/<cedula>')
def get_contact(cedula):
    data = Nomina.query.filter_by(cedula=cedula).first()
    if not data:
        abort(404)
    return render_template('edit-contact.html', nomina = data)

@app.route('/update/<cedula>', methods=['GET', 'POST', 'PUT'])
def update_contact(cedula):
    data = Nomina.query.filter_by(cedula=cedula).first()
    if not data:
        abort(404)
    if data:
        data.fullname = request.form['fullname']
        data.sueldobas = request.form['sueldobas'] 
        data.bono = request.form['bono']            
        db.session.query(Nomina).get(cedula)
        db.session.commit()
        flash('Contacto modificado satisfactoriamente')
        return redirect(url_for('index'))

@app.route('/delete/<cedula>', methods=['GET','POST'])
def delete_contact(cedula):
    data = Nomina.query.filter_by(cedula=cedula).first()
    if request.method == 'POST':
        if data:
            db.session.delete(data)
            db.session.commit()
            return redirect(url_for('index'))
        abort(404)
    flash('Contacto eliminado satisfactoriamente')
    return render_template('delete.html')
