from flask import Flask, render_template, request, flash, redirect, url_for, session
from mysql import connector
import json

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
        db = connection.cursor()
        db.execute("SELECT title, options, answer FROM questions")
        all_questions = db.fetchall()
        
        quiz_questions = []

        for question in all_questions:
            current_question = {
                'title' : question[0],
                'options' : json.loads(question[1]),
                'answer' : question[2]
            }
            quiz_questions.append(current_question)


        # quiz_questions = json.dumps(quiz_questions)
        # return quiz_questions
        # return all_questions
        return render_template('quiz.html',user_name=user_name,questions=quiz_questions)
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

@app.route('/test',methods=['GET','POST'])
def test():
    if request.method == 'GET':
        return render_template('test.html')
    else:
        first_name = request.form.getlist('first_name')
        return first_name
        # return request.form

@app.route('/questions')
def questions():
    db = connection.cursor()
    db.execute("SELECT * FROM questions")
    all_questions =  db.fetchall()
    db.close()

    # return all_questions
    # options = json.loads(all_questions[3][2])
    # return options[0]

    return render_template('questions.html',questions = all_questions)

@app.route('/add-question',methods=['GET','POST'])
def add_question():
    if request.method == 'GET':
        return render_template('add_question.html')
    else:
        errors = False
        options_error = False
        title = request.form.get('title')
        options = request.form.getlist('options')
        answer = request.form.get('answer')


        if not title:
            flash('Title is required','danger')
            errors = True

        for option in options:
            if not option:
                if not options_error:
                    options_error = True
                    errors = True
                    flash('All options are required','danger')
                    break

        if not answer:
            flash('Correct answer is required','danger')
            errors = True

        if errors:
            return redirect( url_for('add_question'))
        else:
            # type casting
            options = json.dumps(options)

            # return options
            db = connection.cursor()
            db.execute("INSERT INTO questions (title,options,answer) VALUES(%s,%s,%s)",(title,options,answer))
            connection.commit()
            db.close()

            flash('New Question Added successfully!','success')
            return redirect(url_for('questions'))



if __name__ == '__main__':
    app.run(debug=True)