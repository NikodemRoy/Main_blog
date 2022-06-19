from django.shortcuts import render
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



def submit_comment(request, blogpost_id):
    url = request.META.get('HTTP_REFERER')

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            data = CommentForm()
            if '/en/' in request.PATH:
                data.text_en = form.cleaned_data['text_en']
                data.text_pl = None
            elif '/pl/' in request.PATH:  
                data.text_pl = form.cleaned_data['text_pl']
                data.text_en = None
            else: 
                raise Http404("Internal page error")   

            data.user_name = form.cleaned_data['user_name']
            data.user_email = form.cleaned_data['user_email']
            data.review = form.cleaned_data['review']
            data.id = request.META.get('REMOTE_ADDR')
            data.project_id = blogpost_id
            data.save()
            # messages.success(request, "Thank You! Review has been submitted.")
            return redirect(url)
