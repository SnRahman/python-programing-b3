from flask import Flask, render_template, request, flash, redirect, url_for, session
from mysql import connector

app = Flask(__name__)
app.secret_key = 'lskjdfslkfjlksjflksjflslfkjsd'
connection = connector.connect(host='127.0.0.1',user='root',password='',database='flask-auth-b3')


@app.route('/')
def index():
    if 'user_name' in session:
        return render_template('dashboard.html')
    else:
        flash('kindly login first!','danger')
        return redirect(url_for('login'))


@app.route('/quiz')
def quiz():
    return render_template('quiz.html')


@app.route('/todo')
def todo():
    return render_template('todo.html')


@app.route('/weather')
def weather():
    return render_template('weather.html')


@app.route('/signup',methods=['GET','POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    else:
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if first_name and email and password and confirm_password and password == confirm_password:
            db = connection.cursor()
            db.execute("INSERT INTO users (first_name,last_name,email,password) VALUES(%s,%s,%s,%s) ",(first_name,last_name,email,password))
            connection.commit()
            db.close()
            flash('User registered successfully!','success')
            return redirect(url_for('index'))
        else:
            flash('Invalid information','danger')
            return redirect(url_for('signup'))


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:

        email = request.form['email']
        password = request.form['password']

        if email and password:
            db = connection.cursor()
            db.execute('SELECT * FROM users WHERE email = %s AND password=%s',(email,password))
            user = db.fetchone()
            db.close()

            if user is not None:
                session['user_id'] = user[0]
                session['user_name'] = f'{user[1]} {user[2]}'

                flash('login Successfully!','success')
                return redirect(url_for('index'))
            
                # return render_template('test.html',user=user)
            else:
                flash('No User Found!', 'danger')
        else:
            flash('Invalid credentials!', 'danger')
        
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session.pop('user_id',None)
    session.pop('user_name',None)

    flash('user logged out Successfully!','success')
    return redirect(url_for('login'))




if __name__ == '__main__':
    app.run(debug=True)