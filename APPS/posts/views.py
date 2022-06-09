from django.shortcuts import render

# Create your views here.

def post(request, post_detail):
    context = {}
    return render(request, 'posts/single_post.html' )