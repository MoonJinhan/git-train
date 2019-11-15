from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"boards.html")


def subway_order(request):
    name = request.POST.get("name")
    date = request.POST.get("date")
    sandwitch = request.POST.get("sandwitch")
    size = request.POST.get("size")
    bread = request.POST.get("bread")
    # 여러 체크리스트를 받아올땐 getlist
    source = request.POST.getlist("source") 

    context = {
        'name': name,
        'date': date,
        'sandwitch':sandwitch,
        'size': size,
        'bread': bread,
        'source': ", ".join(source)
    }

    return render(request, 'django_orm/subway_result.html', context)

def subway_result(request):
    return render(request,' django_orm/subway.html')