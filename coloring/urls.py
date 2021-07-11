from django.urls import path
from . import views

urlpatterns = [
    path('demo', views.index, name='demo'),
    path('new_interaction', views.index, name='new_interaction')
]
