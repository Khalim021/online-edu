# Generated by Django 3.2.4 on 2021-06-23 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_alter_speakermodel_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeaturesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25, verbose_name='title')),
                ('duration', models.IntegerField(verbose_name='duration')),
                ('lecture', models.IntegerField(verbose_name='lecture')),
                ('quizzes', models.IntegerField(verbose_name='quizzes')),
                ('students', models.IntegerField(verbose_name='students')),
                ('price', models.FloatField(verbose_name='price')),
                ('real_price', models.FloatField(verbose_name='real_price')),
                ('price_discount', models.FloatField(verbose_name='price_discount')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
            ],
            options={
                'verbose_name': 'feature',
                'verbose_name_plural': 'features',
            },
        ),
    ]