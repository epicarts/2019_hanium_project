# chat/urls.py
from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
    #url(r'^$',views.index , name='index'),
    #url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
]
