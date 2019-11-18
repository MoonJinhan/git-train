from django.urls import path
from .import views

app_name="subway"
#app이 여러개 될 때,name이 겹칠 경우 위의 app_name을 설정한다.
urlpatterns =[

    #name 을 설정하면 url관리가 수월해 집니다..
    #python 파일 안쪽에서는 'app_name:설정name'
    #template 에서는 (% url 'app_name:설정' %)
    #url이 바뀌어도 일일이 찾아서 바꿀 필요가 없다.

    path('/',views.index,name='index'),
    path('name/',views.name,name='name'),
    path('creat/',views.creat,name='creat'),
    # redirect('app_name:설정name' 넘길 id)
    #(% url'설정name' 넘길 id %)
    path('detail/<int:id>',views.detail,name='detail'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),

]