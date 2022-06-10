from django.shortcuts import render
from APPS.blog.models import BlogPost

from django.shortcuts import get_object_or_404

# Create your views here.

def post(request, post_slug):
    post_detail = get_object_or_404(BlogPost, translations__slug = post_slug)
    print(post_slug)
    context = {'post_detail':post_detail}
    return render(request, 'posts/single_post.html', context )