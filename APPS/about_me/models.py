from django.db import models

from parler.models import TranslatableModel, TranslatedFields

class Shortdescription(TranslatableModel):
    translations = TranslatedFields(
        up_text = models.CharField(max_length=255),
        down_text = models.CharField(max_length=255),
    )
    photo = models.ImageField(upload_to='profile', default='profile/user.png')
    email = models.EmailField(max_length=255, blank=True),

    fb_link = models.CharField(max_length=255, blank=True),
    github_link = models.CharField(max_length=255, blank=True),
    linkedin_link = models.CharField(max_length=255, blank=True),
    instagram_link = models.CharField(max_length=255, blank=True),

    class Meta:
        verbose_name = "Short"
        verbose_name_plural = 'Short'

    def __str__(self):
        return self.email
