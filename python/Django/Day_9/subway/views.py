from django.shortcuts import render,redirect
from .models import Subway

# Create your views here.
def index(request):
    subways = Subway.objects.all()
    context = {
        'subways':subways
    }
    return render(request,'subways/index.html',context)

def new(request):
    if request.method == "POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        menu = request.POST.get('menu')
        bread = request.POST.get('bread')
        sauce = request.POST.get('sauce')
        veg = request.POST.getlist('veg')
        drink = request.POST.get('drink')

        subway = Subway()
        subway.name = name
        subway.address = address
        subway.phone = phone
        subway.menu = menu
        subway.bread = bread
        subway.sauce = sauce
        subway.vegetable = veg
        subway.drink = drink

        subway.save()

        return redirect('subway:index')
    else:
        return render(request, 'subways/new.html')

# def create(request):
#     name= request.POST.get('name')
#     address= request.POST.get('address')
#     phone = request.POST.get('phone')
#     home= request.POST.get('home')
#     menu= request.POST.get('menu')
#     bread= request.POST.get('bread')
#     source= request.POST.get('source')
#     veg= request.POST.get('veg')
#     drink= request.POST.get('drink')

#     subway=Subwawy()
#     subway.name = name
#     subway.address=address
#     subway.phone =phone
#     subway.home = home
#     subway.menu =menu
#     subway.bread = bread
#     subway.source = source
#     subway.veg =veg
#     subway.drink = drink

#     subway.save()

#     return redirect('/')

def detail(request,id):
    sub = Subway.object.get(id=id)

    context ={

        'sub':sub
    }
    return render(request,'subways/detail.html',context)

def edit(request, art_id):
    subway=Subway.objects.get(id=id)
    if request.method == "POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        menu = request.POST.get('menu')
        bread = request.POST.get('bread')
        sauce = request.POST.get('sauce')
        veg = request.POST.getlist('veg')
        drink = request.POST.get('drink')

        # subway = Subway()
        # subway.name = name
        # subway.address = address
        # subway.phone = phone
        # subway.menu = menu
        # subway.bread = bread
        # subway.sauce = sauce
        # subway.vegetable = veg
        # subway.drink = drink

        # subway.save()

        return redirect('subway:detail', subway.id)
    else:
        context = {
            'subway': subway
        }
        return render(request, 'subway/update.html', context)

# def update(request,art_id):
#     sub = Subway.object.get(id=id)
#     name= request.POST.getlist('name')
#     address= request.POST.getlist('address')
#     phone = request.POST.getlist('phone')
#     home= request.POST.getlist('home')
#     menu= request.POST.getlist('menu')
#     bread= request.POST.getlist('bread')
#     source= request.POST.getlist('source')
#     veg= request.POST.getlist('veg')
#     drink= request.POST.getlist('drink')

#     subway=Subwawy()
#     subway.name = name
#     subway.address=address
#     subway.phone =phone
#     subway.home = home
#     subway.menu =menu
#     subway.bread = bread
#     subway.source = source
#     subway.veg =veg
#     subway.drink = drink

#     subway.save()

#     return redirect('subway:index', sub.id)

def delete(request):    
    if request.method == "POST":
        sub = Subway.objects.get(id=id)
        sub.delete()
        return redirect('subway:index')
    else:
        return redirect('subway:detail',id)

