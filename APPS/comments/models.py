from django.db import models

from APPS.blog.models import BlogPost


class Comment(models.Model):
    project = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='project')

    text_en = models.TextField(max_length=1000, blank=True)
    text_pl = models.TextField(max_length=1000, blank=True)

    is_public = models.BooleanField(default=True)
    user_name = models.CharField(max_length=30)
    user_email = models.EmailField()

    creation_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = 'Comments'

    def __str__(self):
        return f'Project: {self.project}, Date: {self.creation_date}, Email: {self.user_email}'
