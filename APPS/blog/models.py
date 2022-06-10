from django.db import models
from django.shortcuts import render

from parler.models import TranslatableModel, TranslatedFields


class BlogPost(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(max_length=96),
        slug = models.SlugField(max_length=255),
        description= models.TextField(max_length=10000, blank=True),
        publish_date = models.DateTimeField(auto_now=True),
    )

    created_date = models.DateTimeField(auto_now_add=True)
    cover = models.ImageField(upload_to='post_cover', blank=True)
    publish_status = models.BooleanField(default=False)
    comment_count = models.IntegerField(default=0, blank=True)
    heart_count = models.IntegerField(default=0, blank=True)

    tags = models.ManyToManyField('Tag', blank=True)

    
    def __str__(self):
        return self.title


class Tag(TranslatableModel):
    translations = TranslatedFields(
        tag = models.CharField(max_length=96)
    )

    def __str__(self):
        return self.tag


class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=30, blank=False)
    user_email = models.EmailField(blank=False)
    text_en = models.TextField(max_length=1000, blank=False)
    text_pl = models.TextField(max_length=1000, blank=False)

    def __str__(self):
        return self.user_name


class BlogPost2(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(max_length=96),
        slug = models.SlugField(max_length=255),
        description= models.TextField(max_length=10000, blank=True),
        publish_date = models.DateTimeField(auto_now=True),
    )

    created_date = models.DateTimeField(auto_now_add=True)
    cover = models.ImageField(upload_to='post_cover', blank=True)
    publish_status = models.BooleanField(default=False)
    comment_count = models.IntegerField(default=0, blank=True)
    heart_count = models.IntegerField(default=0, blank=True)

