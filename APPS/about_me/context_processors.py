from .models import Shortdescription, Profile

def short_description(request):
    short_description = Shortdescription.objects.get(id=2)
    profile = Profile.objects.get(id=1)
    return {'short_description':short_description, 'profile':profile}

