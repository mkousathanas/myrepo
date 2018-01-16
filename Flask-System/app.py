"""Καλούνται οι παρακάτω λειτουργίες για την εκτέλεση της εφαρμογής"""
from flask import Flask, render_template, request, redirect, url_for, g, session, flash
import sqlite3 as sql
import sqlite3
import hashlib

app = Flask(__name__)
"""Μυστικό κλειδί για session"""
app.secret_key = 'sic@*#^shfido8d5sad8#^&'
"""Συνάρτηση για το Password hashing"""
def check_password(hashed_password, user_password):
    return hashed_password == hashlib.md5(user_password.encode()).hexdigest()
"""Παρακάτω γίνεται η επιβεβαίωση των πεδίων username & Password"""
def validate(username, password):
    con = sqlite3.connect('static/user.db')
    completion = False
    with con:
                cur = con.cursor()
                cur.execute("SELECT * FROM Users")
                rows = cur.fetchall()
                for row in rows:
                    dbUser = row[0]
                    dbPass = row[1]
                    if dbUser==username:
                        completion=check_password(dbPass, password)
    return completion

"""Συνάρτηση για την φόρμα login"""
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        completion = validate(username, password)
        if completion ==False:
            error = 'Eσφαλμένα στοιχεία. Παρακαλώ προσπαθήστε ξανά.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)
"""Συνάρτηση για αποσύνδεση απο την εφαρμογή"""
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out.')
    return redirect(url_for('login'))
	

@app.route('/home.html')
def home():
   return render_template('home.html')

@app.route('/enternew')
def new_student():
   return render_template('register.html')
"""Η παρακάτω συνάρτηση είναι υπέυθυνη για την καταχώριση των εγγραφών στη βάση δεδομένων"""
@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         nm = request.form['nm']
         addr = request.form['add']
         city = request.form['city']
         pin = request.form['pin']
         
         with sql.connect("database.db") as con:
            cur = con.cursor()
            
            cur.execute("INSERT INTO users (name,addr,city,pin)VALUES(?,?,?,?)",(nm,addr,city,pin))
            
            con.commit()
            msg = "Η εγγραφή προστέθηκε με επιτυχία!"
      except:
         con.rollback()
         msg = "Σφάλμα με την καταχώρηση εγγραφής"
      
      finally:
         return render_template("result.html",msg = msg)
         con.close()
"""Για την προβολή εγγραφών απο τη βάση δεδομένων"""
@app.route('/list')
def list():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from users")
   
   rows = cur.fetchall();
   return render_template("list.html",rows = rows)
   

if __name__ == '__main__':
   app.run(debug = True)