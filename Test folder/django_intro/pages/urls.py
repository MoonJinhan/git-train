from django.urls import path
from . import views

urlpatterns = [
    path('user_new/',views.user_new),
    path('index/',views.index)
]