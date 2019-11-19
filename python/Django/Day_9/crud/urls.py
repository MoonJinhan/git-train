from django.urls import path, include
from . import views

app_name="crud"
urlpatterns = [
    path('',views.index,name='index'), #crud/
    path('new/',views.new,name='new'), #crud/new 실행하기위한 것
    path('<int:id>',views.detail,name='detail'),
    path('<int:id>/update/',views.update,name="update"),
    path('<int:id>/delete/',views.delete,name="delete"),
]