from django import views
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact_me, name='contact_me'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('portfolio/project/<int:project>', views.project_detail, name='project_detail'),
    path('search/', views.search, name='search'),
]


