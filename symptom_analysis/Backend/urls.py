from django.urls import path
from .import views

app_name = 'authapp'

urlpatterns = [
    path('login', views.login)
]