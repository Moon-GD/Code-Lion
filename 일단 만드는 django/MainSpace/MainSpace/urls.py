from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('grade/', include('gradeapp.urls')),
    path('display/', include('displayApp.urls')),
]
