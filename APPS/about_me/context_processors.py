from .models import Shortdescription

def short_description(request):
    short_description = Shortdescription.objects.get(id=1)
    return {'short_description':short_description}

