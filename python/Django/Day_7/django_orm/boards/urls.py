from django.urls import path
from . import views

urlpatterns =[
	path('',views.index),
	path('subway_order/', views.subway_order),
	path('subway_result/',views.subway_result),
]