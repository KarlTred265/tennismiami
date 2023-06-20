from django.urls import path
from userapp import views

urlpatterns = [
    path('',views.Home,name="Home")


]
