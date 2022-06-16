from django.shortcuts import render
from .models import BlogPost
from django.db.models import F

from django.shortcuts import get_object_or_404


from .models import Categories, Subcategories
from APPS.about_me.models import Profile
from APPS.projects.models import Mainproject, Projects

from .services import get_search

# pagination
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    posts = BlogPost.objects.filter(publish_status = True).order_by('-created_date')

    
    # pagination
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    page_post = paginator.get_page(page)

    context = {
        'posts':posts,
        'page_post':page_post
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
    posts = BlogPost.objects.filter(publish_status = True, category__translations__slug=subcategory)
  
    # # pagination
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    page_post = paginator.get_page(page)

    context = {
        'posts':posts,
        'page_post':page_post
        }
   
    return render(request, 'blog/home.html', context)



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

