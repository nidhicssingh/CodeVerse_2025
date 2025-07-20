from django.shortcuts import render, HttpResponse


# Create your views here.

def about(request):
    #return HttpResponse("this is about page")
    return render(request,'about.html')


def services(request):
    #return HttpResponse("this is service page")
    return render(request,'services.html')


def contact(request):
    #return HttpResponse("this is contact page")
    return render(request,'contact.html')

def skills(request):
    #return HttpResponse("this is skills page")
    return render(request,'skills.html')

def blogs(request):
    #return HttpResponse("this is blogs page")
    return render(request,'blogs.html')

def certification(request):
    #return HttpResponse("this is certification page")
    return render(request,'certification.html')
  
def projects(request):
    #return HttpResponse("this is projects page")
    return render(request,'projects.html')
