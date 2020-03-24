from django.urls import path
from . import views

urlpatterns = [
    path('', views.EventList.as_view(), name='indexSchedule'),
    path('schedule/0/', views.MonEventsList.as_view(), name='monEvents'),
    path('schedule/1/', views.TueEventsList.as_view(), name='tueEvents'),
    path('schedule/2/', views.WedEventsList.as_view(), name='wedEvents'),
    path('schedule/3/', views.ThuEventsList.as_view(), name='thuEvents'),
    path('schedule/4/', views.FriEventsList.as_view(), name='friEvents'),
    path('schedule/5/', views.SatEventsList.as_view(), name='satEvents'),
    path('schedule/6/', views.SunEventsList.as_view(), name='sunEvents'),
    path('schedule/event/<int:pk>', views.EventDetail.as_view(), name='eventDetail'),
]
