from flask import Flask,render_template,request
import requests
from decouple import config
from pprint import pprint
import random


app=Flask(__name__)

token=config('TOKEN')
base_url=f"https://api.telegram.org/bot{token}"

# @app.route('/telegram')
# def telegram():
#     token=config('TOKEN')
#     base_url=f"https://api.telegram.org/bot{token}"
#     lotto = random.sample(range(1,47),6)

#     chat_id = res['result'][0]['message']['chat']['id']
#     send_url=f'/sendMessage?chat_id={chat_id}&text={lotto}'
#     res =requests.get(base_url).json()
#     # print(lotto)
#     # res = requests.get(f'{base_url}/getUpdates').json()
#     # print(chat_id)
#     pprint(res)

#     return ''

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

# @app.route('/',methods=['POST'])
# def tel_web():
    
#     req = request.get_json().get('message')

#     if req is not None:
#         chat_id = req.get('chat').get('id')
#         text = req.get('text')
#     if '로또' == text:
#         lotto = list_1=['말 많은'], list_2=['늑대'], list_3=['~와 함께 춤을']
#     else:
#         lotto=text

#     send_url = f'/sendMessage?chat_id={chat_id}&text={lotto}'
#     response = requests.get(base_url+send_url)



    # print(chat_id,text)
    # return '', 200 

@app.route('/papago')
def papago():
    C_ID = config('C_ID')
    C_SC =config('C_SC')
    url = 'https://openapi.naver.com/v1/papago/n2mt'

    headers = {
        "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
        "X-Naver-Client-Id": C_ID,
        "X-Naver-Client-Secret": C_SC
    }
    data = {
        "source": "ko",
        "target": "en",
        "text":"안녕하세요."
    }

    req = requests.post(url,headers=headers,data=data).json()
    print(req)
    return"Finish!"

@app.route('/',methods=['POST'])
def tel_web():
    
    C_ID = config('C_ID')
    C_SC =config('C_SC')
    url = 'https://openapi.naver.com/v1/papago/n2mt'
    req = request.get_json().get('message')
    
    headers = {
        "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
        "X-Naver-Client-Id": C_ID,
        "X-Naver-Client-Secret": C_SC
    }

    if req is not None:
        chat_id = req.get('chat').get('id')
        text = req.get('text')

    if '로또' in text:
        mag =random.sample(range(1,47),6)

    elif "/번역" in text:
        #/번역 내용
        re_txt = text.replace("/번역","")
        data = {
            "source": "ko",
            "target": "en",
            "text":"안녕하세요."
        }
        res = requests.post(url,headers=headers,data=data).json()
        print(res)
        msg = res.get('message').get('result').get('translatedText')
    
    else:
        msg = text

    send_url = f'/sendMessage?chat_id={chat_id}&text={msg}'
    response = requests.get(base_url+send_url)
    return "",200

if __name__=="__main__":
    app.run(debug=True)