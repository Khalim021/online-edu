# Generated by Django 3.2.4 on 2021-06-19 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PartnerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='logo', verbose_name='logo')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='updated_at')),
            ],
            options={
                'verbose_name': 'partner',
                'verbose_name_plural': 'partners',
            },
        ),
    ]