from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name="Home"),
    path("signup", views.signup, name="Signup"),
    path("login", views.login, name="Login"),
    path("login1", views.login1, name="Login")
    
]
