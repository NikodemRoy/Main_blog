# Generated by Django 4.0.4 on 2022-06-19 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='is_new',
            field=models.BooleanField(default=True),
        ),
    ]