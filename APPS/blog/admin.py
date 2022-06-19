from django.contrib import admin
from parler.admin import TranslatableAdmin, TranslatableTabularInline

from django.db import models
from django.utils.safestring import mark_safe
from django.contrib.admin.widgets import AdminFileWidget

from .models import BlogPost, Tag, Categories, Subcategories, PostImages
from APPS.comments.models import Comment

# inline images preview
class AdminImageWidget(AdminFileWidget):

    def render(self, name, value, attrs=None, renderer=None):
        output = []

        if value and getattr(value, "url", None):
            image_url = value.url
            file_name = str(value)

            output.append(
                f'<a href="{image_url}" target="_blank">'
                f'<img src="{image_url}" alt="{file_name}" width="150" height="150" '
                f'style="object-fit: cover;"/> </a>')

        output.append(super(AdminFileWidget, self).render(name, value, attrs, renderer))
        return mark_safe(u''.join(output))



class BlogPostInline(admin.TabularInline):
    model = PostImages
    extra = 0
    formfield_overrides = {
    models.ImageField: {'widget': AdminImageWidget}
    }

class CommentsInline(admin.StackedInline):
    model = Comment
    readonly_fields = ('text_en', 'text_pl', 'user_name', 'user_email', 'ip')
    extra = 0

class BlogPostAdmin(TranslatableAdmin):
    inlines = [BlogPostInline, CommentsInline]


# admin.site.register(PostImages)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Tag, TranslatableAdmin)
admin.site.register(Categories, TranslatableAdmin)
admin.site.register(Subcategories, TranslatableAdmin)
