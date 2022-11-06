from django.db import models

from APPS.about_me.models import Profile

from parler.models import TranslatableModel, TranslatedFields

class Mainproject(TranslatableModel):
    translations = TranslatedFields(
        project_name = models.CharField(max_length=255),
        slug = models.CharField(max_length=255, blank=True),

        project_shortdescription = models.CharField(max_length=2550, blank=True),
        project_fulldescription = models.TextField(max_length=25500, blank=True),
        # description= RichTextField(max_length=10000, blank=True),
        github_link = models.CharField(max_length=255, blank=True),
    )
    
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    stack = models.ManyToManyField('stack', blank=True)
    is_public = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='project_cover', blank=True)
    image = models.ImageField(upload_to='project_image', blank=True)

    class Meta:
        verbose_name = "Mainproject"
        verbose_name_plural = 'Mainprojects'

    def __str__(self):
        return self.project_name

class Projects(TranslatableModel):
    translations = TranslatedFields(
        project_name = models.CharField(max_length=255),
        slug = models.CharField(max_length=255, blank=True),

        project_shortdescription = models.CharField(max_length=2550, blank=True),
        project_fulldescription = models.TextField(max_length=25500, blank=True),
        github_link = models.CharField(max_length=255, blank=True),
    )

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    stack = models.ManyToManyField('stack', blank=True)
    is_public = models.BooleanField(default=False)
    
    image = models.ImageField(upload_to='project_image', blank=True)


    class Meta:
        verbose_name = "Project"
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.project_name

class Stack(TranslatableModel):
    translations = TranslatedFields(
        stack = models.CharField(max_length=96)
    )

    class Meta:
        verbose_name = "Stack"
        verbose_name_plural = 'Stack'

    def __str__(self):
        return self.stack

class MainprojectImage(models.Model):
    main_project = models.ForeignKey(Mainproject, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_image', blank=True)
    alt_pl = models.CharField(max_length=255, blank=True)
    alt_en = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f'project: {self.main_project}'

class ProjectImage(models.Model):
    main_project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_image', blank=True)
    alt_pl = models.CharField(max_length=255, blank=True)
    alt_en = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f'project: {self.main_project}'
