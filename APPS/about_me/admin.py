from django.contrib import admin

# Register your models here.
from django.contrib import admin
from parler.admin import TranslatableAdmin, TranslatableInlineModelAdmin, TranslatableStackedInline

from .models import Mainskill, Profile, Shortdescription, Skill, Message

class ShortdescriptionInline(TranslatableStackedInline):
    model = Shortdescription
    extra = 0

class SkillInline(TranslatableStackedInline):
    model = Skill
    extra = 0

class ProfileAdmin(TranslatableAdmin):
    inlines = [ShortdescriptionInline, SkillInline]

class MessageAdmin(admin.ModelAdmin):
    list_display = ("subject", "name", "email", "creation_date")
    readonly_fields = ("subject", "name", "email", "creation_date", "ip", "receiver")

admin.site.register(Shortdescription, TranslatableAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Mainskill, TranslatableAdmin)
admin.site.register(Skill, TranslatableAdmin)
admin.site.register(Message, MessageAdmin)

