from django.shortcuts import render
from .models import BlogPost

from .models import Categories, Subcategories

# pagination
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    posts = BlogPost.objects.filter(publish_status = True)
    
    
    # cat_list = []
    # category_list = Categories.objects.all()
    # for category in category_list:
    #     cat_list.append(category)
    # print(cat_list)
    # sub = Subcategories.objects

    # pagination
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
    main_projects = [1,2,3,]
    other_projects = [1,2,3,4]
    context = {
        'main_projects':main_projects,
        'other_projects':other_projects
        }
    print("main_projects")   
    return render(request, 'blog/portfolio.html', context)


def project_detail(request, project):
    context = {}
    return render(request, 'blog/project_detail.html', context)

