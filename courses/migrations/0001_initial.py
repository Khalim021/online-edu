# Generated by Django 3.2.4 on 2021-06-19 08:51

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=17, verbose_name='title')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='SpeakerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='name')),
                ('image', models.ImageField(default=False, upload_to='image', verbose_name='image')),
                ('bio', models.TextField(verbose_name='bio')),
                ('about', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='about')),
                ('avatar', models.ImageField(default=False, upload_to='avatar', verbose_name='avatar')),
                ('job', models.CharField(default=False, max_length=35, verbose_name='job')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
            ],
            options={
                'verbose_name': 'speaker',
                'verbose_name_plural': 'speakers',
            },
        ),
        migrations.CreateModel(
            name='CourseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=175, verbose_name='title')),
                ('image', models.ImageField(upload_to='courses', verbose_name='image')),
                ('overview', models.TextField(verbose_name='overview')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('categories', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='courses.categorymodel', verbose_name='categories')),
                ('speakers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='courses.speakermodel', verbose_name='speaker')),
            ],
            options={
                'verbose_name': 'course',
                'verbose_name_plural': 'courses',
            },
        ),
    ]
