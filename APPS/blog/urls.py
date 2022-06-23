from django import views
from django.urls import path

# from django.conf import settings
# from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('top/', views.home_top, name='home_top'),
    path('category/<str:subcategory>', views.home_category, name='home_category'),
    path('contact/', views.contact_me, name='contact_me'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('portfolio/project/<str:project>', views.project_detail, name='project_detail'),
    path('search/', views.search, name='search'),
    path('submit-comment/<int:blogpost_id>/', views.submit_comment, name='submit_comment'),
    path('save-post/', views.save_post, name='save_post'),
    path('reaction-count/<int:blogpost_id>/', views.reaction_count, name='reaction_count'),
    path('read-later/', views.read_later, name='read_later'),
]

# serving media files
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


