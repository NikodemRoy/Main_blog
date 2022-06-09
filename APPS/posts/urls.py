from django import views
from django.urls import path

from . import views

urlpatterns = [
    path('<int:post_detail>', views.post, name='post')
]


