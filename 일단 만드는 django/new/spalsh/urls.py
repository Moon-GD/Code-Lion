from django.urls import path
from spalsh import views
urlpatterns = [
    path('', views.start),
]