# Generated by Django 3.2.4 on 2021-06-25 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_commentmodel_coursecommentmodel'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CommentModel',
            new_name='SpeakerCommentModel',
        ),
    ]
