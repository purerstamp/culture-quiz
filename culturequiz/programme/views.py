from datetime import date
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from programme.models import Event

class EventList(ListView):
  model = Event
  def lun():
    return "Lundi"
  def mar():
    return "Mardi"
  def mer():
    return "Mercredi"
  def jeu():
    return "Jeudi"
  def ven():
    return "Vendredi"
  def sam():
    return "Samedi"
  def dim():
    return "Dimanche"
  __switcher = {
    1: lun,
    2: mar,
    3: mer,
    4: jeu,
    5: ven,
    6: sam,
    7: dim
  }
  def numToStr(num):
    func = switcher.get(num, "Error while getting current day.")
    return func()
  dateCur = numToStr(date.today().weekday())
  datePlus1 = numToStr((date.today().weekday() + 1) % 7)
  datePlus2 = numToStr((date.today().weekday() + 2) % 7)
  datePlus3 = numToStr((date.today().weekday() + 3) % 7)
  datePlus4 = numToStr((date.today().weekday() + 4) % 7)
  datePlus5 = numToStr((date.today().weekday() + 5) % 7)
  datePlus6 = numToStr((date.today().weekday() + 6) % 7)
  datePlus7 = numToStr((date.today().weekday() + 7) % 7)

# Create your views here.
#def index(request):
#    return HttpResponse("Ici, retrouvez le programme de la semaine.")
#
# Program of the day
#def potd(request, day):
#   return HttpResponse("Programme de %s" % day)
