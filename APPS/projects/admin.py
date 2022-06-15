from django.contrib import admin
from parler.admin import TranslatableAdmin

from .models import Mainproject, Projects, Stack

admin.site.register(Mainproject, TranslatableAdmin)
admin.site.register(Projects, TranslatableAdmin)
admin.site.register(Stack, TranslatableAdmin)

