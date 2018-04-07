from django.urls import path

from . import views


app_name = 'auths'
urlpatterns = [
    # localhost:8000/login
    path('', views.login, name='login'),
]
