from django.shortcuts import render
from APPS.blog.models import BlogPost
from APPS.comments.models import Comment

from django.shortcuts import get_object_or_404
from django.http import Http404

# Create your views here.

def post(request, post_slug):
    post_detail = get_object_or_404(BlogPost, translations__slug = post_slug)
   
   
    # comments = Comment.objects.filter(project__translations__slug=post_slug)
    if '/en/' in request.path:
        comments = Comment.objects.filter(project=post_detail, text_pl='')

    elif '/pl/' in request.path:  
        comments = Comment.objects.filter(project=post_detail, text_en='')
    else: 
        raise Http404("Internal page error") 
    print(comments)
    context = {
        'post_detail':post_detail,
        'comments':comments,
        }
    return render(request, 'posts/single_post.html', context )