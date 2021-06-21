from django.http import HttpResponse


def index(request):
    return HttpResponse('Workflow')


def second_page(request):
    return HttpResponse('Workflow page2')
