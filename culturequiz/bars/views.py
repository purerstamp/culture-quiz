#from django.shortcuts import render
#from django.http import HttpResponse
from django.views.generic import ListView
from .models import Bar

class BarList(ListView):
  """
    This view is part of the bars app.
    Return all bars. Use this view for the bars index.
  """
  context_object_name = 'bars_list'
  template_name = 'bars/bars_list.html'
  model = Bar
