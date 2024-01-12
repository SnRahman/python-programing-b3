from flask import Flask, render_template, request, redirect, url_for
from mysql.connector import connect


# from mysql import connector
# connection = connector.connect()


app = Flask(__name__)
connection = connect(host='localhost',user='root',password='',database='flask-3-b3')

@app.route('/')
def home():
    db = connection.cursor()
    db.execute('SELECT * FROM users')
    users = db.fetchall()
    return render_template('home.html',users=users)


@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/register', methods=['POST'])
def register():
    # return request.form
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    confirm_password = request.form['confirm_password']

    if first_name and last_name and email and password and confirm_password and password == confirm_password:
        
        db = connection.cursor()
        db.execute('INSERT INTO users (first_name,last_name,email,password) VALUES(%s,%s,%s,%s)',(first_name,last_name,email,password))
        connection.commit()
        db.close()

        return redirect(url_for('home'))
    else:
        return redirect(url_for('signup'))









if __name__ == '__main__':
    app.run(port=8000,debug=True)