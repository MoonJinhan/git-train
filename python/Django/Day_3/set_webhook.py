from decouple import config
import requests
from pprint import pprint

token=config('TOKEN')
base_url=f"https://api.telegram.org/bot{token}"

url="answls7337.pythonanywhere.com/"
# url='f7393776.ngrok.io'
setweb_url = f'/setWebhook?url={url}'

req =requests.get(base_url+setweb_url).json()

pprint(req)
