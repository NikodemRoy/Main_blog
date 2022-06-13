from django.contrib import admin

# Register your models here.
from django.contrib import admin
from parler.admin import TranslatableAdmin

from .models import Mainskill, Profile, Shortdescription, Skill

admin.site.register(Shortdescription, TranslatableAdmin)
admin.site.register(Profile, TranslatableAdmin)
admin.site.register(Mainskill, TranslatableAdmin)
admin.site.register(Skill, TranslatableAdmin)

