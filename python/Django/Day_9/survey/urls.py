from django.urls import paht, include
from . import views

app_name="survey"
urlpatterns = [
    path=('', views.index, name ='index'),
    path=('new/',views.new, name ='new'),
    
]
    