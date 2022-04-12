from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Hello Django! Learning by Django's tutorial")


def my_poll(request):
    return HttpResponse("Hello Django! Testing!")
