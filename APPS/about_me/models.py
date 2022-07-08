from email import message
from django.db import models

from parler.models import TranslatableModel, TranslatedFields

class Shortdescription(TranslatableModel):
    translations = TranslatedFields(
        up_text = models.CharField(max_length=255),
        down_text = models.CharField(max_length=255),
        fb_link = models.CharField(max_length=255, blank=True),
        github_link = models.CharField(max_length=255, blank=True),
        linkedin_link = models.CharField(max_length=255, blank=True),
        instagram_link = models.CharField(max_length=255, blank=True),
        email = models.CharField(max_length=255, blank=True),
    )
    photo = models.ImageField(upload_to='profile', default='profile/user.png')

    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, default=None, null=True, blank=True)

    class Meta:
        verbose_name = "Short"
        verbose_name_plural = 'Short'

    def __str__(self):
        return self.email

class Profile(TranslatableModel):
    translations = TranslatedFields(
        full_text = models.TextField(max_length=2550),
        contact_me_up = models.CharField(max_length=255, blank=True),
        contact_me_down = models.CharField(max_length=255, blank=True),
    )

    class Meta:
        verbose_name = "Profil"
        verbose_name_plural = 'Profil'

    def __str__(self):
        return f"this is my porofile {self.id}"


class Mainskill(TranslatableModel):
    translations = TranslatedFields(
        skill_name = models.CharField(max_length=2550),
        skill_description = models.CharField(max_length=2550),
    )

    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)

    def __str__(self):
        return self.skill_name


class Skill(TranslatableModel):
    translations = TranslatedFields(
        skill_name = models.CharField(max_length=255),
    )

    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)

    def __str__(self):
        return self.skill_name
    
class Message(models.Model):
    receiver = models.ForeignKey(Profile, on_delete=models.SET_NULL, default=None, null=True, blank=True)
    creation_date = models.DateField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    ip = models.CharField(max_length=2550, blank=True)

    name = models.CharField(max_length=96, blank=False)
    email = models.EmailField(max_length=96, blank=False)
    subject = models.CharField(max_length=96, blank=False)
    message = models.TextField(max_length=9600, blank=False)

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = 'Messages'

    def __str__(self):
        return f'Subject: {self.subject}, Email: {self.email}, Date: {self.creation_date}'