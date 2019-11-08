from flask import Flask,render_template,request
import requests
from decouple import config
from pprint import pprint
import random


app=Flask(__name__)

token=config('TOKEN')
base_url=f"https://api.telegram.org/bot{token}"

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/send_msg')
def send_msg():
    req = request.args.get("chat")
    #받을때
    res = requests.get(f'{base_url}/getUpdates').json()
    chat_id = res['result'][0]['message']['chat']['id']

    send_url = f'/sendMessage?chat_id={chat_id}&text={req}'

    response = requests.get(base_url+send_url)
    #보낼때
    return "보내기 완료"

@app.route('/telegram')
def telegram():
    token=config('TOKEN')
    base_url=f"https://api.telegram.org/bot{token}"
    lotto = random.sample(range(1,47),6)

    chat_id = res['result'][0]['message']['chat']['id']
    send_url=f'/sendMessage?chat_id={chat_id}&text={lotto}'
    res =requests.get(base_url).json()
    # print(lotto)

    # res = requests.get(f'{base_url}/getUpdates').json()
    # print(chat_id)
    pprint(res)

    return ''



if __name__=="__main__":
    app.run(debug=True)