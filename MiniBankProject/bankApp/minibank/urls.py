from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('register/', views.register, name='register'),
    path('register/add/',views.add, name='add'),
    path('login/',views.login, name='login'),
    path('login/userlogin/',views.userlogin, name='userlogin'),
]