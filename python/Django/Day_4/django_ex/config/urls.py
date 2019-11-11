"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pages import views
#pages 에 있는 views를 가지고 오는것.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    # path('<int:age>/',views.age),
    path('<int:Squared>/',views.Squared),
    path('plus/<int:num1>/<int:num2>',views.cal),
    path('profile/<str:name>/<int:age>',views.profile),
    path('indian/<str:name>',views.indian),
    path('lotto/', views.lotto ),
    path('job/<str:name>',views.job),
    path('image/',views.image),
    path('dtl/',views.dtl),
    path('birthday/',views.birthday),
]


#집배원과 같은 역할