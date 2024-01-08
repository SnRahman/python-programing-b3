from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return 'welcome'

@app.route('/home')
def home():
    return 'HOme page'

@app.route('/shop')
def shop():
    return 'Shop page'

@app.route('/contact')
def contact():
    return 'Contact page'


@app.route('/babloo')
def babloo():
    return 'Hello Babloo!'

# @app.route('/name/<float:n>')
@app.route('/name/<float:n>')
# @app.route('/name/<n>')
def name(n):
    return f'<h1> My Name is : {n} </h1>'

@app.route('/redirect')
def redirect_google():
    # return redirect('https://www.facebook.com')
    # return url_for('home')
    return redirect( url_for('home') )

@app.route('/redirect-to/<name>')
def redirect_to(name):

    # return redirect( url_for(name) )

    if name == 'index':
        return redirect( url_for('index') )
    elif name == 'shop':
        return redirect( url_for('shop') )
    elif name == 'contact':
        return redirect( url_for('contact') )
    else:
        return 'function name out of scope.'
    return name






if __name__ == '__main__':
    app.run(debug=True)