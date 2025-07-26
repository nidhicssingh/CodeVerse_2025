from django.shortcuts import render

def home(request):
    return render(request, 'codeverse/home.html')

def events(request):
    return render(request, 'codeverse/events.html')

def profile(request):
    return render(request, 'codeverse/profile.html')

def gallery(request):
    return render(request, 'codeverse/gallery.html')

def sessions(request):
    return render(request, 'codeverse/sessions.html')
