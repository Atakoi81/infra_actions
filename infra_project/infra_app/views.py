from django.http import HttpResponse


def index(request):
    return HttpResponse('У меня пока не все получилось!, но!!!')


def second_page(request):
    return HttpResponse('А это вторая страница!')
