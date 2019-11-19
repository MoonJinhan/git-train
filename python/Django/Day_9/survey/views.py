from django.shortcuts import render
from .models import Survey
# Create your views here.
def index(request):
    s
    return render(request,'survey/index.html')

def new(request):
    if request.method =="POST":
        q = request