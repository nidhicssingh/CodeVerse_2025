from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('projects/', views.projects, name='projects'),
    path('blogs/', views.blogs, name='blogs'),
    path('skills/', views.skills, name='skills'),
    path('education/', views.education, name='education'),
    path('services/', views.services, name='services'),
    path('certification/', views.certification, name='certification'),
]
