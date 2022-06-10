from django import views
from django.urls import path

from . import views

urlpatterns = [
    path('xD/', views.about_me, name='about_me')
]


