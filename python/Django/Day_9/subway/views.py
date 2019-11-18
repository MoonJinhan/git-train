from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    subways = subway.object.all()
    context = {
        'subways':subways
    }
    return render(request,'subways/index.html',context)

def name(request):
    return render(request,'subways/name.html')

def creat(request):
    name= request.POST.get('name')
    address= request.POST.get('address')
    phone = request.POST.get('phone')
    home= request.POST.get('home')
    menu= request.POST.get('menu')
    bread= request.POST.get('bread')
    source= request.POST.get('source')
    veg= request.POST.get('veg')
    drink= request.POST.get('drink')

    subway=Subwawy()
    subway.name = name
    subway.address=address
    subway.phone =phone
    subway.home = home
    subway.menu =menu
    subway.bread = bread
    subway.source = source
    subway.veg =veg
    subway.drink = drink

    subway.save()

    return redirect('/')

def detail(request,id):
    sub = Subways.object.get(id=id)
    context ={

        'sub':sub
    }
    return render(request,'subways/detail.html',context)

def edit(request, id):
    
    return render(request,)

def update(request,id):
    sub = Subway.object.get(id=id)
    name= request.POST.getlist('name')
    address= request.POST.getlist('address')
    phone = request.POST.getlist('phone')
    home= request.POST.getlist('home')
    menu= request.POST.getlist('menu')
    bread= request.POST.getlist('bread')
    source= request.POST.getlist('source')
    veg= request.POST.getlist('veg')
    drink= request.POST.getlist('drink')

    subway=Subwawy()
    subway.name = name
    subway.address=address
    subway.phone =phone
    subway.home = home
    subway.menu =menu
    subway.bread = bread
    subway.source = source
    subway.veg =veg
    subway.drink = drink

    subway.save()

    return redirect('subway:index' sub.id)

def delete(request):    



    sub.delete()
    return redirect('subway:index')
