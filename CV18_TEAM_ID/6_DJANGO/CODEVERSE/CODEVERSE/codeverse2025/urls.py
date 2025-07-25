from django.contrib import admin
from django.urls import path
from codeverse2025 import views

urlpatterns = [
     path("", views.home, name='home'),
     path('about',views.about, name='about'),
     path('contact',views.contact, name='contact'),
     path('skills',views.skills, name='skills'),
     path('events',views.events, name='events'),
     path('projects',views.projects, name='projects'),
     path('gallery',views.gallery, name='gallery'),     
     
]