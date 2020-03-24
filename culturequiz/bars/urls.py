from django.urls import path
from . import views

urlpatterns = [
    path('', views.BarList.as_view()),
]
