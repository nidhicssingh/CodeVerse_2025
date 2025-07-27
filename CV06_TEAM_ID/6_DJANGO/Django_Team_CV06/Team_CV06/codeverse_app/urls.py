from django.contrib import admin
from django.urls import path
from codeverse_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('events/', views.events, name='events'),
    path('featured/', views.featured, name='featured'),
    path('event1/', views.event1, name='event1'),
    path('event2/', views.event2,name='event2'),
    path('event3/', views.event3,name='event3'),
    path('event4/', views.event4,name='event4'),
    path('event5/', views.event5,name='event5'),
    path('event6/', views.event6,name='event6'),
    path('gallery/', views.gallery,name='gallery'),
]