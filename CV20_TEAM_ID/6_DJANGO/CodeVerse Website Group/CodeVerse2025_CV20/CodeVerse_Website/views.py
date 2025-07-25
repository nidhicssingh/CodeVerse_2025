from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def programs(request):
    return render(request, 'programs.html')

def schedule(request):
    return render(request, 'schedule.html')

def featured(request):
    return render(request, 'featured.html')

def faculties(request):
    return render(request, 'faculties.html')

def participants(request):
    return render(request, 'participants.html')

def blogs(request):
    return render(request, 'blog.html')