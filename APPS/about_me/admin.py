from django.contrib import admin

# Register your models here.
from django.contrib import admin
from parler.admin import TranslatableAdmin, TranslatableInlineModelAdmin, TranslatableStackedInline

from .models import Mainskill, Profile, Shortdescription, Skill

class ShortdescriptionInline(TranslatableStackedInline):
    model = Shortdescription
    extra = 0

class SkillInline(TranslatableStackedInline):
    model = Skill
    extra = 0

class ProfileAdmin(TranslatableAdmin):
    inlines = [ShortdescriptionInline, SkillInline]


admin.site.register(Shortdescription, TranslatableAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Mainskill, TranslatableAdmin)
admin.site.register(Skill, TranslatableAdmin)

