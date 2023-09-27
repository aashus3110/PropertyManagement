from django.contrib import admin
from django.urls import path
from apps import views

urlpatterns = [
    path("",views.index, name='apps'),
    path('signup', views.handleSignUp, name='handleSignUp'),
    path('login', views.handeLogin, name='handleLogin'),
    path('logout', views.handelLogout, name='handleLogout'),
    path('propsell',views.propsell, name='propsell'),
    path('buy',views.buy, name='buy'),
    path('cdata',views.cdata, name='cdata'),
    path('pdata',views.pdata, name='pdata'),
    path('search', views.search, name='search'),
    path('Contact', views.Contact, name='Contact'),
]
