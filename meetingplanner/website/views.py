from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from meetings.models import Meeting, Room

def welcome(request):
    return render(request, "website/welcome.html", {'meetings': Meeting.objects.all()})

def date(request):
    return HttpResponse("This page was served at " + str(datetime.now()))

def about(request):
    return HttpResponse("Hello and welcome to my webpage, this is a starter site to get used to working with the django"
                        "web framework using python")



