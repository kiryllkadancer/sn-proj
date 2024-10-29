from django.apps import apps

from .models import Course, PublishStatus


def get_publish_courses():
    Course = apps.get_model('courses', 'Course')
    return Course.objects.all()
