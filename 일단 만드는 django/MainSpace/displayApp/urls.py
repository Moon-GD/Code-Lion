from django.urls import path
from displayApp import views

urlpatterns = [
    path('first/', views.first),
    path('second/', views.second),
]
