from django.contrib import admin

# Register your models here.
from django.contrib import admin
from parler.admin import TranslatableAdmin

from .models import Shortdescription

admin.site.register(Shortdescription, TranslatableAdmin)

