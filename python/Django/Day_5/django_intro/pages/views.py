from django.shortcuts import render
from pprint import pprint
import random

def throw(request):
    return render(request,'pages/throw.html')

def catch(request):
    # pprint(request)
    # pprint(request.path)
    # pprint(request.method)
    # pprint(request.META)
    message = request.GET.get('message')
    message2 = request.GET.get('message')
    context={
        'msg':message,
        'msg2':message2
    }
    return render(request, 'pages/catch.html', context)

def lotto(request):
    return render(request,'pages/lotto.html')

def lottoresult(request):
    co = request.GET.get('count')
    # request로 넘어오는 값 중 GET방식의 count 를 얻을 것이다.
    print(type(co))

    count=int(request.GET.get('count')) #형병환 해주는 코드
    lotto_num=[]
    for i in range(count):
        lotto_num.append(random.sample(range(1,46), 6)) #랜덤한 로또번호 추출해서 넣어준다.
    context = {
        'count' : count ,
        'lotto' : lotto_num
    }
    return render(request, "pages/result.html", context)

    

