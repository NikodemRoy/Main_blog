from django.contrib import admin
from parler.admin import TranslatableAdmin, TranslatableTabularInline

from django.db import models
from django.utils.safestring import mark_safe
from django.contrib.admin.widgets import AdminFileWidget

from .models import BlogPost, Tag, Categories, Subcategories, Comment

# inline images
# class AdminImageWidget(AdminFileWidget):

#     def render(self, name, value, attrs=None, renderer=None):
#         output = []

#         if value and getattr(value, "url", None):
#             image_url = value.url
#             file_name = str(value)

#             output.append(
#                 f'<a href="{image_url}" target="_blank">'
#                 f'<img src="{image_url}" alt="{file_name}" width="150" height="150" '
#                 f'style="object-fit: cover;"/> </a>')

#         output.append(super(AdminFileWidget, self).render(name, value, attrs, renderer))
#         return mark_safe(u''.join(output))



class BlogPostInline(admin.TabularInline):
    model = Comment
    extra = 1

class BlogPostAdmin(TranslatableAdmin):
    inlines = [BlogPostInline]


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Tag, TranslatableAdmin)
admin.site.register(Categories, TranslatableAdmin)
admin.site.register(Subcategories, TranslatableAdmin)
