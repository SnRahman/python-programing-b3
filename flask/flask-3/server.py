from flask import Flask, render_template, request, redirect, url_for ,flash
from mysql.connector import connect



# from mysql import connector
# connection = connector.connect()


app = Flask(__name__)
connection = connect(host='localhost',user='root',password='',database='flask-3-b3')

app.secret_key = 'sdfhksjhdfkshkjfdhkjshfdkjshkfjskj' 


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

    if first_name and email and password and confirm_password and password == confirm_password:
        
        db = connection.cursor()
        db.execute('INSERT INTO users (first_name,last_name,email,password) VALUES(%s,%s,%s,%s)',(first_name,last_name,email,password))
        connection.commit()
        db.close()
        flash('User Registered Successfully!','success')
        
        return redirect(url_for('home'))
    else:
        return redirect(url_for('signup'))

@app.route('/edit/<id>',methods=['GET','POST'])
def edit(id):
    if request.method == 'GET':
        db = connection.cursor()
        db.execute(f'SELECT id,first_name,last_name,email FROM users WHERE id={id}')
        user = db.fetchone()
        return render_template('edit_form.html',user=user)
    else:
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']


        if first_name and email:
            db = connection.cursor()
            db.execute('UPDATE users SET first_name = %s , last_name = %s , email = %s WHERE id = %s',(first_name,last_name,email,id))
            connection.commit()
            db.close()

    return f'updated: {id}'


@app.route('/delete/<id>')
def delete(id):
    db = connection.cursor()
    db.execute('DELETE FROM users WHERE id=%s',(id,))
    connection.commit()
    db.close()

    return f'deleted: {id}'







if __name__ == '__main__':
    app.run(port=8000,debug=True)