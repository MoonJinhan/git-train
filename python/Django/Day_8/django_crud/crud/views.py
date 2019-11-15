from django.shortcuts import render, redirect
from .models import Article
# Create your views here.
def index(request):
    #순서 1번 방법
    # articles = Article.objects.all()[::-1]

    # context ={
    #     "articles":articles

    #순서 2번 방법
    articles = Article.objects.order_by('-id')
    #쿼리를 썼을 때만 order_by 사용 가능

    context ={
        "articles":articles

    }

    return render(request,'crud/index.html',context)

def new(request):
    return render(request,'crud/new.html')

# form 에서 데이터를 받아서 DB에 저장을 할 것이다. 그리고 성공메세지 띄우기
def create(request):
    
    title = request.POST.get('title')
    content = request.POST.get('content')
    print(request.GET.get('title'))
    #DB에 저장을 시킬 차례
    article = Article()
    article.title = title
    article.content =content
    article.save()

    
    return render(request,'crud/created.html')

def detail(request,pk):
    #pk=pk 가 (id__exact=pk)랑 같음.
    article=Article.objects.get(pk=pk)
    #pk(안에 있는) = pk(받아오는 pk) 

    context = {
        "article":article
    }
    return render(request, 'crud/detail.html',context)

def update(request,pk):
    article=Article.objects.get(pk=pk)

    context={
        "article":article
    }
    return render(request,'crud/update.html' , context)

def revise(request,pk):
    article = Article.objects.get(pk=pk)
    title = request.POST.get('title')
    content = request.POST.get('content')
    print(title)
    article.title = title
    article.content = content

    article.save()
    return redirect(f'/crud/{article.id}/article/')\

def delete(request,pk):

    article = Article.objects.get(pk=pk)
    article.delete()

    return redirect('/crud/')




