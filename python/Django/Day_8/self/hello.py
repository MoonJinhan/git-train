from flask import Flask

app =Flask(__name__)

@app.route('/')
def hello():
    name = "world!!"
    return f'hello {name} !!'