from flask import Flask, render_template,request
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
    return render_template('menu.html', menu=order)

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

@app.route('/fake_naver')
def fake_naver():
    return render_template('fake_naver.html')

@app.route('/fake_google')
def fake_google():
    return render_template('fake_google.html')

@app.route('/send')
def send():
    return render_template('send.html')

@app.route('/receive')
def receive():
    name=request.args.get('name')
    message = request.args.get('message')
    return render_template('receive.html',name=name,msg=message)

@app.route('/birth')
def birth():
    return render_template('birth.html')

@app.route('/indian1')
def indian():
    year = request.args.get('year')
    month = request.args.get('month')
    date =request.args.get('date')
    return render_template('indian.html', year=year,month=month,date=date)

@app.route('/indian')
def indian():
    return render_template(indian1.html):

@app.route('/indian_result')
def result():
    list_1=['말 많은'],
    list_2=['늑대'],
    list_3=['~와 함께 춤을']

    l1 =random.choice(list_1)
    l2 = random.choice(list_2)
    l3 = random.choice(list_3)
if __name__=="__main__":
    app.run(debug=True, port=8000)