from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from programme.models import Event

class EventList(ListView):
  model = Event

# Create your views here.
#def index(request):
#    return HttpResponse("Ici, retrouvez le programme de la semaine.")
#
# Program of the day
#def potd(request, day):
#   return HttpResponse("Programme de %s" % day)
