from django.urls import path
from . import views

urlpatterns = [
    path('', views.logging, name='logging')
]
