from django.contrib import admin
from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ('project', 'is_public', 'is_new', 'creation_date')
    list_filter = ('project', 'is_public', 'is_new')
    
admin.site.register(Comment, CommentAdmin)
