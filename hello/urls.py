from django.contrib import admin
from django.urls import path
from  hello import views

urlpatterns = [
    path('',views.logged ,name='login' ),
    path('home',views.index, name='home' ),
    path('clubs',views.clubs,name='clubs' ),
    path('logout',views.loggedOut,name='logout'),
    path('sign', views.signed ,name = 'sign' ),
    # path('template',views.temple ,name = 'template'),
    path('acad',views.academy,name='acad' ),
    path('sports',views.sports,name='sports' ),
    path('query',views.query,name='query' ),
    path('event',views.event,name='event' ),
    path('form',views.formed,name='form' ),
    path('answer',views.answered,name='answer' ),
    path('button',views.button,name='button' )
    

]