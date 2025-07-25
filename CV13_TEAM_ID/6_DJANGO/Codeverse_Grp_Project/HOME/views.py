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

def home(request):
    #return HttpResponse("this is contact page")
    return render(request,'home.html')

def education(request):
    #return HttpResponse("this is contact page")
    return render(request,'education.html')

def skills(request):
    #return HttpResponse("this is contact page")
    return render(request,'skills.html')

def blogs(request):
    #return HttpResponse("this is contact page")
    return render(request,'blogs.html')

def certification(request):
    #return HttpResponse("this is contact page")
    return render(request,'certification.html')
def projects(request):
    #return HttpResponse("this is contact page")
    return render(request,'projects.html')

# In your Django views.py (or a similar context where you prepare data)
def schedule_view(request):
    schedule_data = [
    {
        "date_day": "14/7/25\nMonday",
        "time": "11.15 am to\n12.30 pm",
        "section": "A",
        "topics_outcome": "• GITHUB hands-on\n• Example",
        "expert": "NA"
    },
    {
        "date_day": "14/7/25\nMonday",
        "time": "11.15 am to\n12.30 pm",
        "section": "B",
        "topics_outcome": "NA",
        "expert": "NA"
    },
    {
        "date_day": "14/7/25\nMonday",
        "time": "11.15 am to\n12.30 pm",
        "section": "C",
        "topics_outcome": "NA",
        "expert": "Ms. Nidhi Singh\nMs. Banesori Ayekpam"
    },
    {
        "date_day": "14/7/25\nMonday",
        "time": "12.30 pm to\n12.45 pm",
        "section": "A\nB",
        "topics_outcome": "Quick Calm: 15-Minute Yoga",
        "expert": "NA\nNA"
    },
    {
        "date_day": "14/7/25\nMonday",
        "time": "12.30 pm to\n12.45 pm",
        "section": "C",
        "topics_outcome": "NA",
        "expert": "Ms. Kunj Verma"
    },
    {
        "date_day": "14/7/25\nMonday",
        "time": "1.45 pm-\n3.15 pm",
        "section": "A",
        "topics_outcome": "Overview of Tkinter standard GUI\nlibrary for Python with example",
        "expert": "NA"
    },
    {
        "date_day": "14/7/25\nMonday",
        "time": "1.45 pm-\n3.15 pm",
        "section": "B\nC",
        "topics_outcome": "Task :-\n• \"Build a Team Calculator with\nCustom Features\" (Team Work)\n• Build a Python-based quiz app\n(Team work).",
        "expert": "NA\nMs. Nidhi Singh\nMs. Banesori Ayekpam"
    },
    {
        "date_day": "15/7/25\nTuesday",
        "time": "11.15 am to\n12.30 pm",
        "section": "A",
        "topics_outcome": "• GITHUB hands-on",
        "expert": "NA"
    },
    {
        "date_day": "15/7/25\nTuesday",
        "time": "11.15 am to\n12.30 pm",
        "section": "B",
        "topics_outcome": "• Example",
        "expert": "Ms. Nidhi Singh\nMs. Banesori Ayekpam"
    },
    {
        "date_day": "15/7/25\nTuesday",
        "time": "11.15 am to\n12.30 pm",
        "section": "C",
        "topics_outcome": "NA",
        "expert": "NA"
    },
    {
        "date_day": "15/7/25\nTuesday",
        "time": "12.30 pm to\n12.45 pm",
        "section": "A",
        "topics_outcome": "Quick Calm: 15-Minute Yoga",
        "expert": "NA"
    },
    {
        "date_day": "15/7/25\nTuesday",
        "time": "12.30 pm to\n12.45 pm",
        "section": "B",
        "topics_outcome": "NA",
        "expert": "Ms. Kunj Verma"
    },
    {
        "date_day": "15/7/25\nTuesday",
        "time": "12.30 pm to\n12.45 pm",
        "section": "C",
        "topics_outcome": "NA",
        "expert": "NA"
    },
    {
        "date_day": "15/7/25\nTuesday",
        "time": "1.45 pm -\n3.15 pm",
        "section": "A",
        "topics_outcome": "Overview of Tkinter standard GUI",
        "expert": "NA"
    },
    {
        "date_day": "15/7/25\nTuesday",
        "time": "1.45 pm -\n3.15 pm",
        "section": "B\nC",
        "topics_outcome": "library for Python with example\nTask :-\n• \"Build a Team Calculator with\nCustom Features\" (Team Work)\n• Build a Python-based quiz app\n(Team work).",
        "expert": "Ms. Nidhi Singh\nMs. Banesori Ayekpam\nNA"
    },
    {
        "date_day": "16/7/25\nWednesday",
        "time": "11.15 am to\n12.30 pm",
        "section": "A",
        "topics_outcome": "• GITHUB hands-on\n• Example",
        "expert": "Ms. Nidhi Singh\nMs. Banesori Ayekpam"
    },
    {
        "date_day": "16/7/25\nWednesday",
        "time": "11.15 am to\n12.30 pm",
        "section": "B",
        "topics_outcome": "NA",
        "expert": "NA"
    },
    {
        "date_day": "16/7/25\nWednesday",
        "time": "11.15 am to\n12.30 pm",
        "section": "C",
        "topics_outcome": "NA",
        "expert": "NA"
    },
    {
        "date_day": "16/7/25\nWednesday",
        "time": "12.30 pm to\n12.45 pm",
        "section": "A",
        "topics_outcome": "Quick Calm: 15-Minute Yoga",
        "expert": "Ms. Kunj Verma"
    },
    {
        "date_day": "16/7/25\nWednesday",
        "time": "12.30 pm to\n12.45 pm",
        "section": "B",
        "topics_outcome": "NA",
        "expert": "Mr. Ritik Nagar"
    },
    {
        "date_day": "16/7/25\nWednesday",
        "time": "12.30 pm to\n12.45 pm",
        "section": "C",
        "topics_outcome": "NA",
        "expert": "NA"
    },
    {
        "date_day": "16/07/25\nWednesday",
        "time": "1.45 pm-\n3.15 pm",
        "section": "A",
        "topics_outcome": "Overview of Tkinter standard GUI library for Python with example",
        "expert": "Ms. Nidhi Singh\nMs. Banesori Ayekpam"
    },
    {
        "date_day": "16/07/25\nWednesday",
        "time": "1.45 pm-\n3.15 pm",
        "section": "B\nC",
        "topics_outcome": "Task :-\n• \"Build a Team Calculator with\nCustom Features\" (Team Work)\n• Build a Python-based quiz app\n(Team work).",
        "expert": "NA\nNA"
    },
    {
        "date_day": "17/7/25\nThursday",
        "time": "9.30-11.00 am",
        "section": "A",
        "topics_outcome": "Overview:- Tkinter, Turtle, Pygame,",
        "expert": "Ms. Shylaja B\nDr. Amal MR"
    },
    {
        "date_day": "17/07/25\nThursday",
        "time": "9.30-11.00 am",
        "section": "B",
        "topics_outcome": "Advanced problem related to python (Using Pygame, Tkinter, Turtle libraries and framework): spotify song search, WhatsApp Message Generator",
        "expert": "Ms. Banesori Ayekpam\nMs. Tamizh Arasi G S"
    },
    {
        "date_day": "17/07/25\nThursday",
        "time": "9.30-11.00 am",
        "section": "C",
        "topics_outcome": "Multithreaded Web Crawler, GUI Social Media Post Like System, TO DO list GUI",
        "expert": "Ms. Nidhi Singh\nMr. Shine V.J"
    },
    {
        "date_day": "17/07/25\nThursday",
        "time": "11.15 am to\n12.30 pm",
        "section": "A",
        "topics_outcome": "Overview:- Tkinter, Pygame, Turtle",
        "expert": "Ms. Shylaja B\nDr. Amal MR"
    },
    {
        "date_day": "17/07/25\nThursday",
        "time": "11.15 am to\n12.30 pm",
        "section": "B",
        "topics_outcome": "Advanced problem related to python (Using Pygame, Tkinter, Turtle libraries and framework): spotify song search, WhatsApp Message Generator",
        "expert": "Ms. Tamizh Arasi G S\nMs. Banesori Ayekpam"
    },
    {
        "date_day": "17/07/25\nThursday",
        "time": "11.15 am to\n12.30 pm",
        "section": "C",
        "topics_outcome": "Multithreaded Web Crawler, GUI Social Media Post Like System, TO DO list GUI, Mini Social Media app using Python's standard GUI library tkinter, Game using Python Pygame Framework, Graphics problem (Drawing and Art using Python's turtle)",
        "expert": "Mr. Shine V.J\nMs. Nidhi Singh"
    },
    {
        "date_day": "17/07/25\nThursday",
        "time": "12.30 pm to\n12.45 pm",
        "section": "A",
        "topics_outcome": "Quick Calm: 15-Minute Yoga",
        "expert": "Ms. Kunj Verma"
    },
    {
        "date_day": "17/07/25\nThursday",
        "time": "12.30 pm to\n12.45 pm",
        "section": "B",
        "topics_outcome": "Quick Calm: 15-Minute Yoga",
        "expert": "Mr. Ritik Nagar"
    },
    {
        "date_day": "17/07/25\nThursday",
        "time": "12.30 pm to\n12.45 pm",
        "section": "C",
        "topics_outcome": "Quick Calm: 15-Minute Yoga",
        "expert": "Mr. Yadla Vishwa Sree"
    },
    {
        "date_day": "17/07/25\nThursday",
        "time": "1.45 pm-\n3.15 pm",
        "section": "A",
        "topics_outcome": "• Django Intro + Setup + Mini Project Kickoff",
        "expert": "Dr. Amal MR\nMs. Shylaja B"
    },
    {
        "date_day": "17/07/25\nThursday",
        "time": "1.45 pm-\n3.15 pm",
        "section": "B",
        "topics_outcome": "",
        "expert": "Ms. Tamizh Arasi G S\nMs. Banesori Ayekpam"
    },
    {
        "date_day": "17/07/25\nThursday",
        "time": "1.45 pm-\n3.15 pm",
        "section": "C",
        "topics_outcome": "",
        "expert": "Ms. Nidhi Singh\nMr. Shine V.J."
    },
    {
        "date_day": "18/07/25\nFriday",
        "time": "9.30-11.00 am",
        "section": "A",
        "topics_outcome": "• Webpage Resume + App (to do list & schedule)",
        "expert": "Dr. Amal MR\nMs. Shylaja B"
    },
    {
        "date_day": "18/07/25\nFriday",
        "time": "9.30-11.00 am",
        "section": "B",
        "topics_outcome": "• App(to do list & schedule)",
        "expert": "Ms. Tamizh Arasi G S\nMs. Banesori Ayekpam"
    },
    {
        "date_day": "18/07/25\nFriday",
        "time": "9.30-11.00 am",
        "section": "C",
        "topics_outcome": "",
        "expert": "Ms. Nidhi Singh\nMr. Shine V.J."
    },
    {
        "date_day": "18/07/25\nFriday",
        "time": "11.15 am to\n12.30 pm",
        "section": "A",
        "topics_outcome": "Django Project:- Website with login page(shopping/any ecommerce website) (Team work)",
        "expert": "Dr. Amal MR\nMs. Shylaja B"
    },
    {
        "date_day": "18/07/25\nFriday",
        "time": "11.15 am to\n12.30 pm",
        "section": "B",
        "topics_outcome": "Django Project:- Website with login page(shopping/any ecommerce website) (Team work)",
        "expert": "Ms. Tamizh Arasi GS\nMs. Banesori Ayekpam"
    },
    {
        "date_day": "18/07/25\nFriday",
        "time": "11.15 am to\n12.30 pm",
        "section": "C",
        "topics_outcome": "",
        "expert": "Ms. Nidhi Singh\nMr. Shine V.J."
    },
    {
        "date_day": "18/07/25\nFriday",
        "time": "12.30 pm to\n12.45 pm",
        "section": "A",
        "topics_outcome": "Quick Calm: 15-Minute Yoga",
        "expert": "Mr. Ritik Nagar"
    },
    {
        "date_day": "18/07/25\nFriday",
        "time": "12.30 pm to\n12.45 pm",
        "section": "B",
        "topics_outcome": "Quick Calm: 15-Minute Yoga",
        "expert": "Ms. Kunj Verma"
    },
    {
        "date_day": "18/07/25\nFriday",
        "time": "12.30 pm to\n12.45 pm",
        "section": "C",
        "topics_outcome": "Quick Calm: 15-Minute Yoga",
        "expert": "Mr. Yadla Vishwa Sree"
    },
    {
        "date_day": "18/07/25\nFriday",
        "time": "1.45 pm-\n3.15 pm",
        "section": "A",
        "topics_outcome": "• HackerRank (Team Work)",
        "expert": "Dr. Amal MR\nMr. Veerendra Reddy\nMs. Shwetha B.N\nMs. Tamizh Arasi G S"
    },
    {
        "date_day": "18/07/25\nFriday",
        "time": "1.45 pm-\n3.15 pm",
        "section": "B",
        "topics_outcome": "",
        "expert": "Ms. Nidhi Singh\nMs. Shylaja B\nMr. Anil Kumar S\nMr. Shine V.J."
    },
    {
        "date_day": "18/07/25\nFriday",
        "time": "1.45 pm-\n3.15 pm",
        "section": "C",
        "topics_outcome": "",
        "expert": "Ms. Banesori Ayekpam\nMr. Somendra Kumar\nMr. Vivek Khirasaria\nDr. Naveen N"
    }
]
    context = {
        'schedule_data': schedule_data,
    }
    return render(request, 'schedule.html', context)

