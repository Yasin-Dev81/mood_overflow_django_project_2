# Generated by Django 4.0.2 on 2022-12-20 18:36

from django.db import migrations, models
import pages.models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_blog_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='cover',
            field=models.ImageField(upload_to=pages.models.blog_cover_directory_path),
        ),
    ]
