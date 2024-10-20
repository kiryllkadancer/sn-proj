# Generated by Django 5.1.2 on 2024-10-20 11:53

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_lessons_can_preview_lessons_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessons',
            name='thumbnail',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='lessons',
            name='video',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='video'),
        ),
    ]
