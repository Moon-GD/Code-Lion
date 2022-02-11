from django.urls import path
from gradeapp import views

urlpatterns = [
    path('', views.grade),
    path('first/', views.first_grade),
]
