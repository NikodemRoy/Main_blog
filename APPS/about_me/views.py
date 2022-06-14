from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Profile
# Create your views here.

def about_me(request):
    profile = get_object_or_404(Profile, id=1)
    main_projects = [1,2,3,]
    context = {
        'main_projects':main_projects,
        'profile':profile,
        }
    print("main_projects")    
    return render(request, 'blog/about_me.html', context)


