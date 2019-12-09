from django.shortcuts import render

# Create your views here.
def user_new(request):
    return render(request, 'pages/user_new.html')

def user_create(request):
    username = request.POST.get('name')
    pw = request.POST.get('pw')

    context={
        'username':username,
        'pw':pw
    }
    
    return render(request, 'pages/user_create.html',context)

def index(request):
        return render(request, 'pages/index.html')