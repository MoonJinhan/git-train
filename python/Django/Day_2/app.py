from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def hello():
    name = "world!!1"
    return f'hello {name}!'

@app.route('/mulcam')
def mulcam():
    return 'hello mulcamp'

@app.route('/greeting/<string:name>')
def greeting(name):
    return f'{name}님 안녕하세요'

@app.route('/lunch/<int:num>')
def lunch(num):
    menu=["짜장면","짜마뽕","공기밥","짜장면곱배기","진한국밥"]
    order = random.sample(menu,num)
    return str(order)

@app.route('/html')
def html():
    mutiline = '''
    <h1> This is H1 Tag </h1>
    <P> this is P tag </P>
    '''
    return mutiline

@app.route('/hi/<string:name>')
def hi(name):
    return render_template('hi.html',name=name)

if __name__=="__main__":
    app.run(debug=True, port=8000)