from django.urls import path

from . import views

urlpatterns = [
    path('', EventList.as_view()),
    path('programme/<str:day>/', views.potd, name='potd'),
]

