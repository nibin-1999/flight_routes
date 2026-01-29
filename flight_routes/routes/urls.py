from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_airport),
    path('search/', views.find_path),
    path('longest/', views.longest_duration),
    path('shortest/', views.shortest_duration),
]
