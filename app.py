from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL 
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

#settings
app.secret_key = 'mysecretkey'

# mysql Connection
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='contactos'
mysql = MySQL(app)

@app.route('/')
def Index():
  cur = mysql.connection.cursor()
  cur.execute('SELECT * FROM nomina')
  data = cur.fetchall()
  return render_template('index.html', nominas = data)

@app.route('/agregar', methods=['POST'])
def addcontact():
    if request.method == 'POST':
      cedula = request.form['cedula']
      fullname = request.form['fullname']
      sueldobas = request.form['sueldobas'] 
      bono = request.form['bono']
      cur = mysql.connection.cursor()
      cur.execute('INSERT IGNORE INTO nomina (cedula, fullname, sueldobas, bono) VALUES (%s, %s, %s, %s)',
      (cedula, fullname, sueldobas, bono))
      cur.execute("""
      UPDATE nomina 
      SET sueldotot = (sueldobas + bono)
      """)
      mysql.connection.commit()
      flash('contacto agregado sactifactoriamente')
      return redirect(url_for('Index'))

@app.route('/edit/<cedula>')
def get_contact(cedula):
  cur = mysql.connection.cursor()
  cur.execute("SELECT * FROM nomina WHERE cedula = %s",[cedula])
  data = cur.fetchall()
  return render_template('edit-contact.html', nomina = data[0])

@app.route('/delete/<string:cedula>')
def delete_contact(cedula):
   cur = mysql.connection.cursor()
   cur.execute('DELETE FROM nomina WHERE cedula = {0}'.format(cedula))
   mysql.connection.commit()
   flash('contacto removido sactisfactoriamente')
   return redirect(url_for('Index'))

@app.route('/update/<cedula>', methods = ['POST'])
def update_contact(cedula):
  if request.method =='POST':
    fullname = request.form['fullname']
    sueldobas = request.form['sueldobas']
    bono = request.form['bono']
    cur = mysql.connection.cursor()
    cur.execute("""
      UPDATE nomina
      SET fullname = %s,
          sueldobas = %s,
          bono = %s,
          sueldotot = (sueldobas + bono)
      WHERE cedula = %s
    """,(fullname, sueldobas, bono, cedula))
    mysql.connection.commit()
    flash('contacto actualizado sactifactoriamente')
    return redirect(url_for('Index'))

if __name__ == '__main__':
    app.run(port = 3000, debug = True)