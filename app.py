from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hey I am running and sending out files to the world 🔥'


if __name__ == '__main__':
    app.run(debug=True)
