from flask import Flask, render_template, request, flash, redirect, url_for, session
from mysql import connector

app = Flask(__name__)
app.secret_key = 'lskjdfslkfjlksjflksjflslfkjsd'
connection = connector.connect(host='127.0.0.1',user='root',password='',database='flask-auth-b3')


@app.route('/')
def index():
    user_name = session.get('user_name',None)
    return render_template('dashboard.html',user_name=user_name)

@app.route('/quiz')
def quiz():
    if 'user_name' in session:
        user_name = session.get('user_name',None)

        return render_template('quiz.html',user_name=user_name)
    else:
        flash('kindly login first!','danger')
        return redirect(url_for('login'))


@app.route('/todo')
def todo():
    if 'user_name' in session:
        user_name = session.get('user_name',None)

        return render_template('todo.html',user_name=user_name)
    else:
        flash('kindly login first!','danger')
        return redirect(url_for('login'))

@app.route('/weather')
def weather():
    if 'user_name' in session:
        user_name = session.get('user_name',None)

        return render_template('weather.html',user_name=user_name)
    else:
        flash('kindly login first!','danger')
        return redirect(url_for('login'))

@app.route('/signup',methods=['GET','POST'])
def signup():
    errors = False
    if request.method == 'GET':
        user_name = session.get('user_name',None)
        return render_template('signup.html',user_name=user_name)
    else:
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        
        if not first_name:
            flash('First name is Required.','danger')
            errors = True
        
        if not email:
            flash('Valid Email is Required.','danger')
            errors = True

        if not password:
            flash('Password is Required.','danger')
            errors = True

        if not confirm_password:
            flash('confirm Password is Required.','danger')
            errors = True

        if password != confirm_password:
            flash('Passwords Should be same','danger')
            errors = True

        if errors:
            return redirect(url_for('signup'))
        else:
            db = connection.cursor()
            db.execute("INSERT INTO users (first_name,last_name,email,password) VALUES(%s,%s,%s,%s) ",(first_name,last_name,email,password))
            connection.commit()
            db.close()
            flash('User registered successfully!','success')
            return redirect(url_for('index'))
        
            


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        user_name = session.get('user_name',None)
        return render_template('login.html',user_name=user_name)
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