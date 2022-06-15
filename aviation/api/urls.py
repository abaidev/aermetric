from django.urls import path
from . import views

app_name = 'aviation-api'

urlpatterns = [
    path('stats/aircraft/<str:craft_model>/', views.aircraft_stats, name='aircraft_stats'),
    path('stats/status/<str:status>/', views.status_stats, name='status_stats'),
    # path('stats/type/<str:type>/', views.type_stats, name='type_stats'),
]
