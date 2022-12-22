# Generated by Django 4.0.2 on 2022-10-07 12:15

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InstaPkForCopy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insta_pk', models.IntegerField()),
                ('status', models.CharField(choices=[('pub', 'published'), ('drf', 'draft')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='InstaUserForCopy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, verbose_name='username for coping')),
                ('user_id', models.CharField(max_length=30, verbose_name='user id for coping')),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='MyInstaPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_key', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('user_id', models.CharField(max_length=20)),
                ('settings', jsonfield.fields.JSONField()),
            ],
        ),
    ]