from django import views
from django.urls import path

from . import views

urlpatterns = [
    path('<str:post_slug>', views.post, name='post')
]


