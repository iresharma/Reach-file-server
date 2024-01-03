from flask import Flask
from r2 import list, create, put

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    list()
    return 'Hey I am running and sending out files to the world 🔥'


@app.route('/create')
def createre():
    create("temp-code-bucket")
    return "OK"

@app.route('/put')
def puter():
    put()
    return "OK"

if __name__ == '__main__':
    app.run(debug=True)
