# Generated by Django 4.0.4 on 2022-07-01 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_me', '0006_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='creation_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]