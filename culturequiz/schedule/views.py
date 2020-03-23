from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from schedule.models import Event

class EventList(ListView):
  context_object_name = 'event_list'
  template_name = 'schedule/event_list.html'
  queryset = Event.objects.all()

  def get_context_data(self, **kwargs):
    context = super(EventList, self).get_context_data(**kwargs)
    context['event_mon_list'] = self.queryset.filter(day__iexact='lundi')
    context['event_tue_list'] = self.queryset.filter(day__iexact='mardi')
    context['event_wed_list'] = self.queryset.filter(day__iexact='mercredi')
    context['event_thu_list'] = self.queryset.filter(day__iexact='jeudi')
    context['event_fri_list'] = self.queryset.filter(day__iexact='vendredi')
    context['event_sat_list'] = self.queryset.filter(day__iexact='samedi')
    context['event_sun_list'] = self.queryset.filter(day__iexact='dimanche')
    return context

# Create your views here.
#def index(request):
#    return HttpResponse("Ici, retrouvez le programme de la semaine.")
#
# Program of the day
#def potd(request, day):
#   return HttpResponse("Programme de %s" % day)
