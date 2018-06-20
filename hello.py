from flask import Flask,url_for
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    context = {
        'name':'xiang',
        'age':27
    }
    return render_template('index.html', context=context)
@app.route('/base')
def base():
    return render_template('base.html')
@app.route('/login')
def login():
    return render_template('login.html')
if __name__ == '__main__':
    app.run(debug = True)