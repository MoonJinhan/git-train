from django.shortcuts import render
from django.http import HttpResponse
import random
import re
from faker import Faker 
from datetime  import datetime


# Create your views here.

# MVC 구조에서 C를 맡고 장고에서는 MVT 구조에서는 V를 맡고 있다. 
# 가장 많은 수정을 거칠 것으로 예상

def index(request):
    #장고는 인덱스 갈호안에 아무젃도 없었는데 장고는 request가 필요
    #return HttpResponse("Hello Django")
    return render(request,'index.html')

# def age(request, age):
#     # 주소의 인자값은 ..
#     # context ={'age':age} 
#     return render(request,'age.html',{'age':age})

def Squared(request, Squared):
    return render(request, 'Squared.html',{'num':Squared**2})

def cal(request, num1, num2):
    context ={
        'num1' : num1,
        'num2' : num2,
        'cal' : num1 + num2
    }
    return render(request, 'plus.html', context)

def profile(request,name,age):
    print(type(name))
    context ={
        'name':name,
        'age':age
    }
    return render(request,'profile.html',context)

def indian(request,name):

    indianname=['집념의 사나이','물을 뿝는 돼지','노망난 아가씨','저리가라 마녀','내가 제일 잘났어 쥐새끼','바지에 똥싼 20대 중반 남성']
    context = {
        'name':name,
        'indianname1': random.choice(indianname)
        }
    return render(request,'indian.html',context)

def lotto(request):
    num = random.sample(range(1,47),6)
    context = {
        'lotto_num':re.sub('\[]','',num)
        #lotto.sort()
        # L_num=[str(I) for I in lotto]
        #context = {
        #   'name':name,
        #   'age': age,
        #   'i_name' : i_name,
        #   'lotto':","
        # }
    }
    return render(request,'lotto.html',context)

def job(request,name):

    fake =Faker('ko_kr')
    job=fake.job()

    context ={
        'name':name,
        'job' : job
    }
    return render(request,'faker_job.html',context)

def image(request):
    num=random.choice(range(1,50))
    url=f"https://picsum.photos/id/{num}/200/300"

    context = {
        'url':url
    }

    return render(request,'image.html',context)
def dtl(request):
    foods = ["짜장면","탕수육","짬뿡","군만두","고추잡채","볶음밥"]
    my_sentence = 'life is hsort, you need python.'
    messages = ['app;e','banna','cucumber','mango']
    timenow = datetime.now() 
    empty_list = []

    context = {

        "foods": foods,
        "my_sentence" : my_sentence,
        "messages":messages,
        "empty_list":empty_list,
        'timenow': timenow
    }
    return render(request,'dtl.html',context)

def birthday(request):
    timenow = datetime.now()
    birth = datetime(2020,7,22)

    d_day = (timenow - birth).days
    #print(today.month)
    if timenow.month == 6 and timenow.date == 22:
        res =  True
    else:
        res = False


    context = {
        'result':res,
        'd_day':d_day
    }   
    # }

    # birthday = ['1991/06/22']

    # context = {
    #     "timenow":timenow,
    #     "birthday":birthday
    # }
    
    return render(request,'birthday.html',context)
