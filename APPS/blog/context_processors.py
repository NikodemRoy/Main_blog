from .models import Categories

def category_list(request):
    category_list = Categories.objects.all()
    return {'category_list':category_list}