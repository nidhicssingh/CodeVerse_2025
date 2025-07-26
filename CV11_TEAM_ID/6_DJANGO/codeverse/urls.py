from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('events/', views.events, name='events'),
    path('profile/', views.profile, name='profile'),
    path('gallery/', views.gallery, name='gallery'),
    path('sessions/', views.sessions, name='sessions'),

]
