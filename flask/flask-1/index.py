from flask import Flask

app = Flask(__name__)

@app.route('/kfc')
def kfc():
    return 'KFC is the best restaurant in China.'

@app.route('/mec')
def mecdolands():
    return 'MEC Dolans are the best theme park in the world. updated'


# app.run()
if __name__ == '__main__':
    app.run(port=8000, debug=True)