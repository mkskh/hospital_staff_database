from django.urls import path
from . import views


app_name = 'staff'

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.reset, name='reset'),
]