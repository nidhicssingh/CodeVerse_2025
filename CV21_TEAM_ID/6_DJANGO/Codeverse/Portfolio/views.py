from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
def education(request):
    return render(request, 'education.html')
def contact(request):
    return render(request, 'contact.html')
def projects(request):
    return render(request, 'projects.html')
def skills(request):
    return render(request, 'skills.html')
def blogs(request):
    return render(request, 'blogs.html')
def certification(request):
    return render(request, 'certification.html')