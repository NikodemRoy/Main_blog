from django.db import models
from django.shortcuts import render

from ckeditor.fields import RichTextField

from parler.models import TranslatableModel, TranslatedFields


class BlogPost(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(max_length=96),
        slug = models.SlugField(max_length=255),
        description= RichTextField(max_length=10000, blank=True),
        publish_date = models.DateTimeField(auto_now=True),
    )

    created_date = models.DateTimeField(auto_now_add=True)
    cover = models.ImageField(upload_to='post_cover', default='post_cover/defoult.png')
    publish_status = models.BooleanField(default=False)
    comment_count = models.IntegerField(default=0, blank=True)
    heart_count = models.IntegerField(default=0, blank=True)

    
    category = models.ForeignKey('Subcategories', on_delete=models.CASCADE, blank=True, null=True )
    tags = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.title

class PostImages(models.Model):
    blogpost = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_image', blank=True)
    alt_pl = models.CharField(max_length=255, blank=True)
    alt_en = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f'Image nr: {self.id}, post: {self.blogpost}'

class Tag(TranslatableModel):
    translations = TranslatedFields(
        tag = models.CharField(max_length=96)
    )

    def __str__(self):
        return self.tag




class Categories(TranslatableModel):
    translations = TranslatedFields(
        category = models.CharField(max_length=96),
        slug = models.SlugField(max_length=255),
    )

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category

class Subcategories(TranslatableModel):
    translations = TranslatedFields(
        subcategory = models.CharField(max_length=96),
        slug = models.SlugField(max_length=255),
    )

    maincategory = models.ForeignKey(Categories, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Subcategory"
        verbose_name_plural = 'Subcategories'
    
    def __str__(self):
        return f'{self.maincategory}: {self.subcategory}'
