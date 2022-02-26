from django.contrib import admin
from django.urls import path
from blogapp import views
from accounts import views as accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('detail/<int:blog_id>', views.detail, name='detail'),
    path('comment_create/<int:blog_id>', views.comment_create, name='comment_create'),
    path('login/', accounts_views.login, name='login'),
    path('logout/', accounts_views.logout, name='logout'),
]
