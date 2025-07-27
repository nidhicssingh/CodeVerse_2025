from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def events(request):
    return render(request, 'events.html')

def featured(request):
    return render(request, 'featured.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def event1(request):
    return render(request, 'event1.html')

def event2(request):
    return render(request, 'event2.html')

def event3(request):
    return render(request, 'event3.html')

def event4(request):
    return render(request, 'event4.html')

def event5(request):
    return render(request, 'event5.html')

def event6(request):
    return render(request, 'event6.html')

def gallery(request):
    return render(request, 'gallery.html')