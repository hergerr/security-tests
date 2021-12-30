from django.urls import path

from . import views

app_name = 'xss'

urlpatterns = [
    path('', views.index, name='index'),
]