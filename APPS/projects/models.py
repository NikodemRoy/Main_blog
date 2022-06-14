from django.db import models

from APPS.about_me.models import Profile

from parler.models import TranslatableModel, TranslatedFields

class Mainproject(TranslatableModel):
    translations = TranslatedFields(
        project_name = models.CharField(max_length=2550),
        project_shortdescription = models.CharField(max_length=2550),
        skill_fulldescription = models.CharField(max_length=2550),
    )

    # profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    stack = models.ManyToManyField('stack', blank=True)
    is_public = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='project_cover', default=None)
    image = models.ImageField(upload_to='project_image', default=None)

    def __str__(self):
        return self.project_name

class projects(TranslatableModel):
    translations = TranslatedFields(
        project_name = models.CharField(max_length=2550),
        project_shortdescription = models.CharField(max_length=2550),
        skill_fulldescription = models.CharField(max_length=2550),
    )

    # profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    stack = models.ManyToManyField('stack', blank=True)
    is_public = models.BooleanField(default=False)
    
    image = models.ImageField(upload_to='project_image', default=None)

    def __str__(self):
        return self.project_name

class Stack(TranslatableModel):
    translations = TranslatedFields(
        stack = models.CharField(max_length=96)
    )

    def __str__(self):
        return self.stack

