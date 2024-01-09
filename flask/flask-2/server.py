from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/register',methods = ['POST','GET'])
def register():
    if request.method == 'GET':
        # return 'register'
        return render_template('register_form.html')
    else:
        if request.files['test_file']:
            test_file = request.files['test_file']
            filename = test_file.filename
            # filename = f'test_file-{test_file.filename}'
            test_file.save('data/' + filename)
        else:
            return 'no file uploaded'

        return request.files['file']




if __name__ == '__main__':
    app.run(debug=True,port=5000)