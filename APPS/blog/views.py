from django.dispatch import receiver
from django.shortcuts import render, redirect
from .models import BlogPost
from django.db.models import F

from django.shortcuts import get_object_or_404, redirect
from django.http import Http404

from .models import Categories, Subcategories

from APPS.about_me.models import Profile, Message
from APPS.about_me.forms import MessageForm

from APPS.projects.models import Mainproject, Projects

from APPS.comments.models import Comment
from APPS.comments.forms import CommentForm
from django.contrib import messages


from .services import get_search

# pagination
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home_redirect(request):
    return redirect(home)
    
def home(request):
    posts = BlogPost.objects.filter(publish_status = True).order_by('-created_date')
    all_post_id = []

    for post in posts:
        all_post_id.append(post.id)
    
    stored_posts = request.session.get("stored_posts")

    if stored_posts is None or len(stored_posts) == 0:
        stored_posts = []
    

 
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
    stored_posts = []
    stored_posts = request.session.get("stored_posts")
    print(f'ALL STOREDPOSTS: {stored_posts}')
  
    context = {
        'posts':posts,
        'stored_posts': stored_posts
        }
   
   
    return render(request, 'blog/read-later.html', context)

def contact_me(request):
    profile = get_object_or_404(Profile, id=1)
    
    context = {'profile':profile}
    return render(request, 'blog/contact_me.html', context)

def send_message(request):
    url = request.META.get('HTTP_REFERER')

    if request.method == "POST":
        form = MessageForm(request.POST)
        message_receiver = get_object_or_404(Profile, id=1)

        if form.is_valid():
            data = Message() 
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            
            data.ip = request.META.get('REMOTE_ADDR')
            data.receiver = message_receiver

            data.save()

            if '/en/' in request.path:
                messages.success(request, "Thank You! Your message has been sent.")
            elif '/pl/' in request.path:  
                messages.success(request, "Dziękuję! Twoja wiadomość została wysłana.")
            return redirect(url)

        else:
            messages.error(request, form.errors)
            return redirect(url)


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

    
    project_test = Projects.objects.filter(translations__slug=project).exists() 
    if project_test:
        project = get_object_or_404(Projects, translations__slug=project) 
        context = {'project':project,}

    mainproject_test = Mainproject.objects.filter(translations__slug=project).exists() 
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

    was_commented = request.session.get("was_commented")
    if was_commented is None or len(was_commented) == 0:
        was_commented = []

    if request.method == "POST":
        form = CommentForm(request.POST)
        # print(form)
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
            
            # checking if post was commented in session 
            was_commented_id = str(project.id)

            if was_commented_id not in was_commented:
                was_commented.append(was_commented_id)
                request.session["was_commented"] = was_commented
                
                print(f'Was commented list ID: {was_commented}')

            if '/en/' in request.path:
                messages.success(request, "Thank You! Comment has been submitted.")
            elif '/pl/' in request.path:  
                messages.success(request, "Dziękuję! Komentarz został dodany.")
            return redirect(url)
        else:
            messages.error(request, form.errors)
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

def reaction_count(request, blogpost_id):
    url = request.META.get('HTTP_REFERER')
    project = get_object_or_404(BlogPost, id=blogpost_id) 
    stored_posts = [] 
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

def page_404(request, exception):
    return render(request, '404.html', status=404)

def page_500(request):
    return render(request, '500.html', status = 500)