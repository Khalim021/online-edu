# Generated by Django 3.2.4 on 2021-06-25 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0003_shopmodel_real_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopCommentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40, verbose_name='first_name')),
                ('last_name', models.CharField(max_length=25, verbose_name='last_name')),
                ('comment', models.TextField(verbose_name='comment')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created-at')),
            ],
            options={
                'verbose_name': 'comment',
                'verbose_name_plural': 'comments',
            },
        ),
    ]
