from django.db import models

from APPS.about_me.models import Profile

from parler.models import TranslatableModel, TranslatedFields

class Mainproject(TranslatableModel):
    translations = TranslatedFields(
        project_name = models.CharField(max_length=255),
        project_shortdescription = models.CharField(max_length=2550, blank=True),
        skill_fulldescription = models.TextField(max_length=25500, blank=True),
        github_link = models.CharField(max_length=255, blank=True),
    )

    # profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    stack = models.ManyToManyField('stack', blank=True)
    is_public = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='project_cover', blank=True)
    image = models.ImageField(upload_to='project_image', blank=True)

    def __str__(self):
        return self.project_name

class projects(TranslatableModel):
    translations = TranslatedFields(
        project_name = models.CharField(max_length=255),
        project_shortdescription = models.CharField(max_length=2550, blank=True),
        skill_fulldescription = models.TextField(max_length=25500, blank=True),
        github_link = models.CharField(max_length=255, blank=True),
    )

    # profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    stack = models.ManyToManyField('stack', blank=True)
    is_public = models.BooleanField(default=False)
    
    image = models.ImageField(upload_to='project_image', blank=True)

    def __str__(self):
        return self.project_name

class Stack(TranslatableModel):
    translations = TranslatedFields(
        stack = models.CharField(max_length=96)
    )

    def __str__(self):
        return self.stack

