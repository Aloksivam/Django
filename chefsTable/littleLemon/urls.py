from django.contrib import admin
from django.urls import path
from . import views,forms
urlpatterns=[
    path('',views.hello,name='hello'),
    path('homepage/',views.homepage,name='homepage'),
    path('date/',views.displaydate,name='displaydate'),
    path('menu/',views.menu,name='menu'),
    path('home/',views.home),
    path('getuser/<name>/<id>',views.pathview,name='pathview'),
    path('getuser/<name>',views.pathview,name='pathview'),
    path('getuser/',views.qryview,name='qryview'),
    path("showform/",views.showform,name='showform'),
    path("getform/",views.getform,name='getform'),
    # path("alok/",name='alok')
    # path("/form",forms.Demoform)
    path('forms/',views.index),
    path('about',views.about), 
    path('menu_card/',views.menu_by_id)
    # path('menu/<int:menu_id>',views.menu_by_id,name='menu_by_id'),
]