from django.shortcuts import render, redirect
from .models import Article
# Create your views here.
def index(request):
    articles = Article.objects.all()

    #순서 1번 방법
    # articles = Article.objects.all()[::-1]

    # context ={
    #     "articles":articles

    #순서 2번 방법
    #articles = Article.objects.order_by('-id')
    #쿼리를 썼을 때만 order_by 사용 가능

    context ={
        "articles":articles
    }

    return render(request,'crud/index.html',context)

def new(request):
    # print(f'new:{request.method}')
    # return render(request, 'crud/new.html') # 기존 new 함수
   
    # REST 하게 바꿨을때 폼이 새로 생성되는 부분.
    if request.method == "POST":
        article =Article(title=request.POST.get('title'),content=request.POST.get('content'))
        article.save()
        return redirect('crud:index')
    else:
    #폼 html 을 불러오는 부분
        return render(request,'crud/new.html')


# form 에서 데이터를 받아서 DB에 저장을 할 것이다. 그리고 성공메세지 띄우기
# def create(request):
    
#     title = request.POST.get('title')
#     content = request.POST.get('content')
#     print(request.GET.get('title'))
#     #DB에 저장을 시킬 차례
#     article = Article()
#     article.title = title
#     article.content =content
#     article.save()

    
    # return render(request,'crud/created.html')

def detail(request,id):
    #pk=pk 가 (id__exact=pk)랑 같음.
    art=Article.objects.get(id=id)
    return render(request,'crud/detail.html',{'art':art}) 
    
    
    # context = {
    #     "article":article
    # }
    # return render(request, 'crud/detail.html',context)

def update(request,id):
    art=Article.objects.get(id=id)

    if request.method =="POST":
        art.tiltle=rquest.POST.get('title')
        art.content=request.POST.get('content')
        art.save() 
        return redirect('crud:detail',art.id)
    else:
        return render(request, 'crud/update.html',{'art':art})
    # context={
    #     "article":article
    # }
    # return render(request,'crud/update.html' , context)

# def revise(request,pk):
#     article = Article.objects.get(pk=pk)
#     title = request.POST.get('title')
#     content = request.POST.get('content')
#     print(title)
#     article.title = title
#     article.content = content

#     article.save()
#     return redirect(f'/crud/{article.id}/article/')\

def delete(request,id):

    art = Article.objects.get(id=id)
    if request.method == "POST":
        art.delete()
        return redirect('crud:index')
    else:
        return redirect('crud:detail',art.id)
    

   


#20191119
#POST art_id/comment

#return redirect('crud:detail',article.id)
#return redirect('crud:detail',com.article_id)
# def comment(request, art_id):
#     article = Article.object.get(id=art_id)

#     if request.method =="POST"
#         comment = request.POST.get('comment')

#         com = Comment()
#         com.comment = comment
#         com.article = article
#         com.save()

# return redirect('crud:detail',art_id)

# def comment_edit(request,art_id,com_id):
#     com = Comment.object.get(id=com_id)

#     if request.method == "POST":
#         text = request.POST.get('comment')
#         com.comment = text 
#         com.save()

#         return redirect('crud:detail', art_id)
#     else
#         return 
#     context = {
#         'conment':com

#     }

#     return render(request, 'crud/comment_edit.html',context)

# def comment_del(request, art_id, com_id):
#     com = Comment.object.get(id =com_id)

#     if request.method == "POST":
#         com.delete()

#     return redirect('crud:detail',art_id)

