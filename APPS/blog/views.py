from django.shortcuts import render

# pagination
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    posts = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]


    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    page_post = paginator.get_page(page)

    context = {
        'posts':posts,
        'page_post':page_post
        }
   
    return render(request, 'blog/home.html', context)

# def home(request):
#     posts = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]


#     paginator = Paginator(posts, 5)
#     page = request.GET.get('page')
#     page_post = paginator.get_page(page)

#     context = {
#         'posts':posts,
#         'page_post':page_post
#         }
#     if request.htmx:
#         return render(request, 'blog/home copy.html', context)
#     return render(request, 'blog/home.html', context)



def contact_me(request):
    context = {}
    return render(request, 'blog/contact_me.html', context)

def about_me(request):
    main_projects = [1,2,3,]
    context = {
        'main_projects':main_projects,
        }
    print("main_projects")    
    return render(request, 'blog/about_me.html', context)


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

