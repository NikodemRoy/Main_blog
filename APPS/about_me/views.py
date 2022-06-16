from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Profile
from APPS.projects.models import Mainproject
# Create your views here.

def about_me(request):
    profile = get_object_or_404(Profile, id=1)
    # main_projects = [1,2,3,]
    main_projects = Mainproject.objects.filter(profile=profile, is_public=True )
    context = {
        'main_projects':main_projects,
        'profile':profile,
        }
    print("main_projects")    
    return render(request, 'blog/about_me.html', context)


