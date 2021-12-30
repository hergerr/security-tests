from django.urls import path

from . import views

app_name = 'xss'

urlpatterns = [
    path('', views.index, name='index'),
    path('script_in_param/', views.param_string)
]