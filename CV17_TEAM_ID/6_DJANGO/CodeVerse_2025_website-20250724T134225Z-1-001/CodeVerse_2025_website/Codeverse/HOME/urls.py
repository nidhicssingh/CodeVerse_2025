from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),            # homepage
    path('about/', views.about, name='about'),    # note the trailing slash
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('certification/', views.certification, name='certification'),
    path('skills/', views.skills, name='skills'),
    path('education/', views.education, name='education'),
    path('blogs/', views.blogs, name='blogs'),
    path('projects/', views.projects, name='projects'),
]

