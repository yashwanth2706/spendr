from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# This view page handles all requests 
def RequestHandler(request):
    return HttpResponse("Hello world")

def home(request):
    return HttpResponse("This is from home function")

def loadTemplate(request):
    template = loader.get_template('homepage.html')
    return HttpResponse(template.render())