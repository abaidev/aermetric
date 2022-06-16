from django.urls import path
from . import views

app_name = 'aviation-api'

urlpatterns = [
    path('stats/aircraft/', views.aircraft_stats, name='aircraft_stats'),
]
