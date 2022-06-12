# Generated by Django 4.0.4 on 2022-06-12 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blogpost_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.categories'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='cover',
            field=models.ImageField(default='post_cover/defoult.png', upload_to='post_cover'),
        ),
    ]