# Generated by Django 5.1.2 on 2024-10-22 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_lessons_thumbnail_lessons_video'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Lessons',
            new_name='Lesson',
        ),
    ]
