from django.shortcuts import render, HttpResponse


# Create your views here.

def about(request):
    #return HttpResponse("this is about page")
    return render(request,'about.html')


def events(request):
    #return HttpResponse("this is events page")
    return render(request,'events.html')


def home(request):
    #return HttpResponse("this is contact page")
    return render(request,'home.html')

def skills(request):
    #return HttpResponse("this is home page")
    return render(request,'skills.html')

def projects(request):
    #return HttpResponse("this is gallery page")
    return render(request,'projects.html')

def contact(request):
    #return HttpResponse("this is contact page")
    return render(request,'contact.html')

def gallery(request):
    #return HttpResponse("this is contact page")
    return render(request,'gallery.html')



