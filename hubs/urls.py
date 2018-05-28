from django.urls import path

from . import views


app_name = 'hubs'
urlpatterns = [
    path('', views.LocationView.as_view(), name='hubs'),
    path('locations', views.LocationView.as_view(), name='locations')
]
