from django.shortcuts import render

from . import services


# Create your views here.
def course_list_view(request):
    queryset = services.get_publish_courses()
    return render(request, 'courses/list.html', {})


def course_detail_view(request):
    return render(request, 'courses/detail.html', {})


def lesson_list_view(request):
    return render(request, 'courses/lesson.html', {})
