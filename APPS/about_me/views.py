from django.shortcuts import render

# Create your views here.

def about_me(request):
    main_projects = [1,2,3,]
    context = {
        'main_projects':main_projects,
        }
    print("main_projects")    
    return render(request, 'blog/about_me.html', context)


