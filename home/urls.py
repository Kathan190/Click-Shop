from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name="Home"),
    path("signup", views.signup, name="Signup"),
    path("login", views.login, name="Login"),
    path("shopinfo", views.shopinfo, name="ShopInfo"),
    path("about", views.about, name="About"),
    path("service", views.service, name="Service"),
    path("contact", views.contact, name="Contact")
]
