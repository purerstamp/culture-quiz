from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from datetime import datetime
from schedule.models import Event

class EventList(ListView):
  """
    This view is part of the schedule app.
    Return all events and all events by day of week. Use this view for the main index.
  """
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

class MonEventsList(ListView):
  """
    This view is part of the schedule app.
    Return all Monday's events. Use this view to build a day-specific page.
  """
  template_name = 'schedule/byDay_events_list.html'
  queryset = Event.objects.filter(day__iexact='lundi')
  def get_context_data(self, **kwargs):
    context = super(MonEventsList, self).get_context_data(**kwargs)
    context['dayOfWeek'] = "Lundi"
    return context

class TueEventsList(ListView):
  """
    This view is part of the schedule app.
    Same as MonEventsList, for Tuesday.
  """
  template_name = 'schedule/byDay_events_list.html'
  queryset = Event.objects.filter(day__iexact='mardi')
  def get_context_data(self, **kwargs):
    context = super(TueEventsList, self).get_context_data(**kwargs)
    context['dayOfWeek'] = "Mardi"
    return context

class WedEventsList(ListView):
  """
    This view is part of the schedule app.
    Same as MonEventsList, for Wednesday.
  """
  template_name = 'schedule/byDay_events_list.html'
  queryset = Event.objects.filter(day__iexact='mercredi')
  def get_context_data(self, **kwargs):
    context = super(WedEventsList, self).get_context_data(**kwargs)
    context['dayOfWeek'] = "Mercredi"
    return context

class ThuEventsList(ListView):
  """
    This view is part of the schedule app.
    Same as MonEventsList, for Thursday.
  """
  template_name = 'schedule/byDay_events_list.html'
  queryset = Event.objects.filter(day__iexact='jeudi')
  def get_context_data(self, **kwargs):
    context = super(ThuEventsList, self).get_context_data(**kwargs)
    context['dayOfWeek'] = "Jeudi"
    return context

class FriEventsList(ListView):
  """
    This view is part of the schedule app.
    Same as MonEventsList, for Friday.
  """
  template_name = 'schedule/byDay_events_list.html'
  queryset = Event.objects.filter(day__iexact='vendredi')
  def get_context_data(self, **kwargs):
    context = super(FriEventsList, self).get_context_data(**kwargs)
    context['dayOfWeek'] = "Vendredi"
    return context

class SatEventsList(ListView):
  """
    This view is part of the schedule app.
    Same as MonEventsList, for Saturday.
  """
  template_name = 'schedule/byDay_events_list.html'
  queryset = Event.objects.filter(day__iexact='samedi')
  def get_context_data(self, **kwargs):
    context = super(SatEventsList, self).get_context_data(**kwargs)
    context['dayOfWeek'] = "Samedi"
    return context

class SunEventsList(ListView):
  """
    This view is part of the schedule app.
    Same as MonEventsList, for Sunday.
  """
  template_name = 'schedule/byDay_events_list.html'
  queryset = Event.objects.filter(day__iexact='dimanche')
  def get_context_data(self, **kwargs):
    context = super(SunEventsList, self).get_context_data(**kwargs)
    context['dayOfWeek'] = "Dimanche"
    return context

class EventDetail(DetailView):
  """
    This view is part of the schedule app.
    Displays details about a particular event.
  """
  template_name = 'schedule/event_detail.html'
  model = Event
  