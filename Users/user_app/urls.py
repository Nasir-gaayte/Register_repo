from django.urls import path
from . import views

urlpatterns = [
    path('',views.base,name='base'),
    path('home/',views.home, name='home'),
    path('register/',views.register, name='register'),
    path('login/',views.login, name='login'),
]
