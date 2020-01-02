from django.urls import path
from . import views
from programme.views import EventList

urlpatterns = [
    path('', EventList.as_view()),
    #path('programme/<str:day>/', views.potd, name='potd'),
]

