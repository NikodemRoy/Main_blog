from django.db.models import Q

from .models import BlogPost

def get_search(request):
    blog_post = None
    if 'search' in request.GET:
        search = request.GET['search'].capitalize() 
        if search:
            blog_post = BlogPost.objects.filter(
                Q(translations__title__icontains= search)|
                Q(tags__translations__tag= search),
                publish_status = True
            ).distinct().order_by('created_date')
        print(search)
    return blog_post