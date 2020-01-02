from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('programme/<str:day>/', views.potd, name='potd'),
]

