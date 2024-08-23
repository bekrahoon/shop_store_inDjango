from django.urls import path, include
from . import views
from store.controller import authview


urlpatterns = [
    path('', views.home, name="home"),
    path('collections', views.collections, name="collections"),
    path('collections/<str:slug>', views.collectionsview, name="collectionsview"),
    path('category/<str:cate_slug>/<str:prod_slug>', views.productveiw, name='productveiw' ),
    
    path("register/", authview.register , name="register"),
    path("login/", authview.loginpage, name="loginpage"),
    path("logout/", authview.logoutpage, name="logout")
]
