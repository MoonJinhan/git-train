from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm,PasswordChangeForm
from django.contrib.auth import login as auth_logi
from django.contrib.auth import logout as auth_logout
from .forms import UserCustomChangeForm
from IPython import embed
from django.contrib.auth import update_session_auth_hash as up_session

def signup(request):
    if request.user.is_authenticated:
        return redirect('boards:index')

    if request.method =="POST":
        form = UserCreationForm(request.POST)
        #embed()
        if form.is_valid():
            user = form.save()
            auth_logi(request, user)
            return redirect('boards:index')

    else:   
        form = UserCreationForm()
        #embed()

    context = {
        'form':form
    }
    return render(request, 'accounts/signup.html', context)

# Create your views here.

def login(request):
    if request.user.is_authenticated:
        return redirect('boards:index')

    if request.method =="POST":
        form = AuthenticationForm(request, request.POST)
        embed()
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or "boards:index")
    else:
        form = AuthenticationForm()

    context ={
        'form':form,
        'label':'로그인'


    }

    return render(request,'accounts/login.html',context)


def logout(request):
    if request.method =="POST":
        auth_logout(request)

        
    auth_logout(request)
    return redirect('boards:index')

def edit(request):
    if request.method =="POST":
        form = UserCustomChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    else: 
        form = UserCustomChangeForm(instance=request.user)

    context = {
        'form' : form,
        'label':'정보수정'
    }

    return render(request,'accounts/edit.html',context)

def chg_pwd(request):
    if request.method =="POST":
        form =PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            form.save()
            up_session(request, user)
            return redirect('accounts:edit')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
        'label':'비번 수정'
    }

    return render(request,'accounts/pwd.html',context)

def delete(request):
        if request.method =="POST":
            request.user.delete()

        return render(request,'accounts/delete.html')
