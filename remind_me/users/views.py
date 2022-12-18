from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse('<center><h1>Welcome to Remind-Me API server!! :)</h1></center>')


def create(request):
    return HttpResponse('<center><h1>Welcome to create!! :)</h1></center>')


def login(request):
    return HttpResponse('<center><h1>Welcome to login!! :)</h1></center>')
