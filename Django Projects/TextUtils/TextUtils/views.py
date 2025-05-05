#This is a custom file
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Hello World</h1>")

def about(request):
    return HttpResponse("This is about page")