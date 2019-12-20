from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Ici, retrouvez le programme de la semaine.")

# Program of the day
def potd(request, day):
   return HttpResponse("Programme de %s" % day)
