from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Azure! This is a Flask web app.'

if __name__ == '__main__':
    app.run(debug=True)
