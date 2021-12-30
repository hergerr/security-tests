from django.urls import path

from . import views
app_name = 'injection'

urlpatterns = [
    path('', views.index, name='index'),
]