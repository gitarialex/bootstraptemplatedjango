from django.shortcuts import render

def homepage(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def eventdetails(request):
    return render(request,'event-details.html')

def rentvenue(request):
    return render(request,'rent-venue.html')

def showsevents(request):
    return render(request,'shows-events.html')

def tickets(request):
    return render(request,'tickets.html')

def ticketdetails(request):
    return render(request,'ticket-details.html')