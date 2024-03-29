from django.contrib import admin
from parler.admin import TranslatableAdmin

from .models import BlogPost, Tag, Categories, Subcategories

class BlogPostAdmin(TranslatableAdmin):
    def get_prepopulated_fields(self, request, obj=None):
        return {
            'slug': ('title',)
        }


admin.site.register(BlogPost, TranslatableAdmin)
admin.site.register(Tag, TranslatableAdmin)
admin.site.register(Categories, TranslatableAdmin)
admin.site.register(Subcategories, TranslatableAdmin)
