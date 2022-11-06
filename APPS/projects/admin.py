from django.contrib import admin
from django.db import models
from parler.admin import TranslatableAdmin

from .models import Mainproject, Projects, Stack, MainprojectImage, ProjectImage

from django.utils.safestring import mark_safe
from django.contrib.admin.widgets import AdminFileWidget


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

class MainprojectInline(admin.TabularInline):
    model = MainprojectImage
    extra = 0
    formfield_overrides = {
    models.ImageField: {'widget': AdminImageWidget}
    }

class MainprojectAdmin(TranslatableAdmin):
    inlines = [MainprojectInline]



class PojectInline(admin.TabularInline):
    model = ProjectImage
    extra = 0
    formfield_overrides = {
    models.ImageField: {'widget': AdminImageWidget}
    }

class ProjectAdmin(TranslatableAdmin):
    inlines = [PojectInline]



admin.site.register(Mainproject, MainprojectAdmin)
admin.site.register(Projects, ProjectAdmin)
admin.site.register(Stack, TranslatableAdmin)

