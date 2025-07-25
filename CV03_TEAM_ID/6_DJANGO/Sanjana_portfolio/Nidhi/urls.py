from django.contrib import admin
from django.urls import path
from Nidhi import views

urlpatterns = [
     path("", views.index, name='base'),
     path('about',views.about, name='about'),
     path('services',views.services, name='services'),
     path('contact',views.contact, name='contact'),
     path('family',views.family, name='family'),
     path('skills',views.skills, name='skills'),
     path('education',views.education, name='education'),
     path('blogs',views.blogs, name='blogs'),
     path('projects',views.projects, name='projects'),
     
     
     
     ]
