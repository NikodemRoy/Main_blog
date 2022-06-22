from django.shortcuts import render, redirect
from .models import BlogPost
from django.db.models import F

from django.shortcuts import get_object_or_404, redirect
from django.http import Http404

from .models import Categories, Subcategories
from APPS.about_me.models import Profile
from APPS.projects.models import Mainproject, Projects
from APPS.comments.models import Comment
from APPS.comments.forms import CommentForm

from .services import get_search

# pagination
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    posts = BlogPost.objects.filter(publish_status = True).order_by('-created_date')
    all_post_id = []

    for post in posts:
        all_post_id.append(post.id)

    stored_posts = request.session.get("stored_posts")

 
    print(f'ALL STOREDPOSTS: {stored_posts}')
    
    # pagination
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    page_post = paginator.get_page(page)

    context = {
        'posts':posts,
        'page_post':page_post,
        'stored_posts': stored_posts
        }
   
    return render(request, 'blog/home.html', context)

def home_top(request):
    posts = BlogPost.objects.filter(publish_status = True).annotate(top=F('comment_count') + F('heart_count')).order_by('-top')

  
    # # pagination
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    page_post = paginator.get_page(page)

    context = {
        'posts':posts,
        'page_post':page_post
        }
   
    return render(request, 'blog/home.html', context)

def home_category(request, subcategory):
    posts = BlogPost.objects.filter(publish_status = True, category__translations__slug=subcategory).distinct().order_by('-created_date')
  
    # # pagination
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    page_post = paginator.get_page(page)

    context = {
        'posts':posts,
        'page_post':page_post
        }
   
    return render(request, 'blog/home.html', context)

def read_later(request):
    posts = BlogPost.objects.filter(publish_status = True).distinct().order_by('-created_date')
    all_post_id = []

    for post in posts:
        all_post_id.append(post.id)
    print(all_post_id)

    stored_posts = request.session.get("stored_posts")
    print(f'ALL STOREDPOSTS: {stored_posts}')
  
    context = {
        'posts':posts,
        'stored_posts': stored_posts
        }
   
   
    return render(request, 'blog/read-later.html', context)

def contact_me(request):
    context = {}
    return render(request, 'blog/contact_me.html', context)


def portfolio(request):
    profile = get_object_or_404(Profile, id=1)

    main_projects = Mainproject.objects.filter(profile=profile, is_public=True)
    
    other_projects = Projects.objects.filter(profile=profile, is_public=True )
    context = {
        'main_projects':main_projects,
        'other_projects':other_projects
        }
    print("main_projects")   
    return render(request, 'blog/portfolio.html', context)


def project_detail(request, project):

    
    project_test = Projects.objects.filter(translations__slug=project) 
    if project_test:
        project = get_object_or_404(Projects, translations__slug=project) 
        context = {'project':project,}

    mainproject_test = Mainproject.objects.filter(translations__slug=project) 
    if mainproject_test:
        mainproject = get_object_or_404(Mainproject, translations__slug=project) 
        context = {'project':mainproject}

    return render(request, 'blog/project_detail.html', context)


def search(request):
    blog_post = get_search(request)
    
    context = {'page_post':blog_post}
    return render(request, 'blog/home.html', context)



def submit_comment(request, blogpost_id):
    url = request.META.get('HTTP_REFERER')
    project = get_object_or_404(BlogPost, id=blogpost_id) 

    if request.method == "POST":
        form = CommentForm(request.POST)
        print(form)
        if form.is_valid():
            data = Comment()
            if '/en/' in request.path:
                data.text_en = form.cleaned_data['text_en']
                data.text_pl = ''
            elif '/pl/' in request.path:  
                data.text_pl = form.cleaned_data['text_pl']
                data.text_en = ''
            else: 
                raise Http404("Internal page error")   
            data.project_id = blogpost_id
            data.user_name = form.cleaned_data['user_name']
            data.user_email = form.cleaned_data['user_email']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            project.comment_count +=1
            project.save()
            return redirect(url)
        else:
            print('data is not valid')
            # messages.success(request, "Thank You! Review has been submitted.")
            return redirect(url)

def save_post(request):
    url = request.META.get('HTTP_REFERER')
    stored_posts = request.session.get("stored_posts")

    if request.method == "POST":
        if stored_posts is None:
            stored_posts = [] 

        post_id = request.POST['post_id']

        if post_id not in stored_posts:
           stored_posts.append(post_id)
           request.session["stored_posts"] = stored_posts
        else:
            stored_posts.remove(post_id)
            request.session["stored_posts"] = stored_posts

        print(f'id of stored posts: {stored_posts}')
    return redirect(url)
