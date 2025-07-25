from django.contrib import admin
from django.urls import path
from CodeVerse_Website import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('programs/', views.programs, name='programs'),
    path('schedule/', views.schedule, name='schedule'),
    path('featured/', views.featured, name='featured'),
    path('faculties/', views.faculties, name='faculties'),
    path('participants/', views.participants, name='participants'),
    path('blog/', views.blogs, name='blog'),
]