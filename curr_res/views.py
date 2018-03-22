from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Current Resident Homepage<h1>")
