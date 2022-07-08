# Generated by Django 4.0.4 on 2022-07-01 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('about_me', '0005_profiletranslation_contact_me_down_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('is_read', models.BooleanField(default=False, null=True)),
                ('ip', models.CharField(blank=True, max_length=2550)),
                ('name', models.CharField(max_length=96)),
                ('email', models.EmailField(max_length=96)),
                ('subject', models.CharField(max_length=96)),
                ('message', models.TextField(max_length=9600)),
                ('profile', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='about_me.profile')),
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
            },
        ),
    ]