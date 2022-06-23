from django.shortcuts import render, redirect
from APPS.blog.models import BlogPost
from APPS.comments.models import Comment

from django.shortcuts import get_object_or_404
from django.http import Http404

from django.db.models import F
# Create your views here.


def post(request, post_slug):
    post_detail = get_object_or_404(BlogPost, translations__slug=post_slug)

    if '/en/' in request.path:
        comments = Comment.objects.filter(project=post_detail, text_pl='', is_public=True)

    elif '/pl/' in request.path:  
        comments = Comment.objects.filter(project=post_detail, text_en='', is_public=True)
    else: 
        raise Http404("Internal page error") 
    
    liked_posts = request.session.get("liked_posts")
    commented_posts = request.session.get("commented_posts")

    was_commented = request.session.get("was_commented")
    if was_commented is None or len(was_commented) == 0:
        was_commented = []
    print(f'Was commentedpost ID: {was_commented}')

   
    context = {
        'post_detail':post_detail,
        'comments':comments,
        'liked_posts':liked_posts,
        'commented_posts':commented_posts,
        'was_commented':was_commented
        }
    return render(request, 'posts/single_post.html', context )

def reactions(request, post_id):
    post = get_object_or_404(BlogPost, id = post_id)
    url = request.META.get('HTTP_REFERER')

    liked_posts = request.session.get("liked_posts")

    if request.method == "POST":
        liked_id = request.POST['liked_id']

        # is post liked
        if liked_id is not None:
            if liked_posts is None:
                liked_posts = [] 

            if liked_id not in liked_posts:
                liked_posts.append(liked_id)
                post.heart_count += 1
                post.save()
                request.session["liked_posts"] = liked_posts
                print(liked_posts)
            else:
                liked_posts.remove(liked_id)
                request.session["liked_posts"] = liked_posts
                post.heart_count -= 1
                post.save()
                print(liked_posts)
                    
    return redirect(url)



        # if request.POST['commented_id']:
        #     # is post commented
        #     commented_id = request.POST['commented_id']

        #     if commented_id is not None:
        #         if commented_posts is None:
        #             commented_posts = [] 

        #         if commented_id not in commented_posts:
        #             commented_posts.append(commented_id)
        #             request.session["commented_posts"] = commented_posts
        #             print(commented_posts)
        #         else:
        #             commented_posts.remove(commented_id)
        #             request.session["commented_posts"] = commented_posts
        #             print(commented_posts)
