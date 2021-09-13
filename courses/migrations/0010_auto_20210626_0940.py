# Generated by Django 3.2.4 on 2021-06-26 04:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_auto_20210626_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursecommentmodel',
            name='courses',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='courses.coursemodel', verbose_name='courses'),
        ),
        migrations.AlterField(
            model_name='speakercommentmodel',
            name='speaker',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='courses.speakermodel', verbose_name='speaker'),
        ),
    ]