
from django.contrib import admin
from django.urls import path,include

app_name="prac"
urlpatterns = [
    path('',views.index)
]