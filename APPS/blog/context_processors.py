from .models import Categories, Tag

def category_list(request):
    category_list = Categories.objects.all()
    return {'category_list':category_list}

def tag_list(request):
    tag_list = Tag.objects.all()
    return {'tag_list':tag_list}