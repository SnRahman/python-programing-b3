from flask import Flask, render_template, request

App = Flask(__name__)

@App.route('/')
def home():
    return 'Welcome to Home page !'

@App.route('/quiz')
def quiz():
    return render_template('quiz.html')

@App.route('/todo')
def todo():
    return render_template('todo.html')

@App.route('/signup')
def signup():
    return render_template('signup.html')

# https methods 
# ['GET','POST','PUT','DELETE','HEAD']
@App.route('/register',methods= ['POST','GET'] )
def register():

    if request.method == 'GET':
        return request.args
    else:
        first_name = request.form['first_name'] 
        last_name = request.form['last_name'] 
        email = request.form['email'] 
        password = request.form['password'] 
        confirm_password = request.form['confirm_password'] 
        # return f'first_name: {first_name} -- Last Name: {last_name} -- Email: {email} -- Password : {password} -- Confirm Password : { confirm_password}'
        
        form_data = request.form

        return render_template('register.html',data=form_data)
        # return first_name
        # return request.form

        return 'form is submited'






App.run(debug = True, port=8080)