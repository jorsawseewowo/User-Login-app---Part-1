from flask import Flask, render_template, request
import mysql.connector
import re
app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    msg=''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        mydb = mysql.connector.connect(
        host="remotemyql.com",
        user="Sussy123",
        password="AmongUs123",
        database="Sussy123",
        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM LoginDetails WHERE Name = %s AND Password = %s", (username, password))
        account = mycursor.fetchone()
        if account:
            print('login success')
            name = account[1]
            id = account[0]
            msg = 'Logged in Successfully'
            print('login successful!')
            return render_template('index.html', msg=msg, name=name, id=id)
        else:
            msg = 'Incorrect Credentials. Please check.'
            return render_template('login.html', msg=msg)
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
    name=''
    id=''
    msg = 'Logged out succesfully'
    return render_template('login.html', msg=msg, name=name, id=id)

@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and username in request.form and password in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        mydb = mysql.connector.connect(
            host = 'remoteysq',
            user='Sussy123',
            password='AmongUs123',
            database='Sussy123',
        )
        mycursor = mydb.cursor()
        print(username)
        mycursor.execute('SELECT * FROM LoginDetails WHERE Name = %s AND Email_id = %s', (username, email))
        account = mycursor.fetchone()
        print(account)
        if account:
            msg = 'Account already exists'
        elif not re.match(r'^[^\d]*\.\.[^\d]*$', email):
            msg = 'Invalid email address'
        elif not re.match(r'(A-Za-z0-9)+', username):
            msg = 'Username must contain only characters and numbers'
        elif not username or not password or not email:
            msg = 'Fill in all the details'
        else:
            mycursor.execute('INSERT INTO LoginDetails VALUES (NULL, %s, %s, %s)', (username, password, email))
            mydb.commit()
            msg = 'Your registration is successful'
            name = username
            return render_template('index.html', msg=msg, name=name)
    elif request.method == 'POST':
        msg = 'Please fill in the details'
        return render_template('registration.html', msg=msg)

if __name__ == '__main__':
    app.run(debug=True)