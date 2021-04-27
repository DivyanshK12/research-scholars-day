from django.shortcuts import render
# from django.http import HttpResponse, Http404, HttpResponseRedirect
# from django.urls import reverse

# Create your views here.
def index(request): # Pass a request object
    #Pass data using context dictionary
    context = {
        "title":"Researchers of IIT Hyderabad"
    }
    return render(request, "index.html", context=context)

def ilrsd(request): # Pass a request object
    #Pass data using context dictionary
    context = {
        "title":"Research Scholars Day | Institute"
    }
    return render(request, "institute.html", context=context)

def dlrsd(request): # Pass a request object
    #Pass data using context dictionary
    context = {
        "title":"Research Scholars Day | Department"
    }
    return render(request, "department.html", context=context)

def seminars(request): # Pass a request object
    #Pass data using context dictionary
    context = {
        "title":"Talks & Seminars"
    }
    return render(request, "seminars.html", context=context)

def links(request): # Pass a request object
    #Pass data using context dictionary
    context = {
        "title":"Important Links"
    }
    return render(request, "links.html", context=context)

def info(request): # Pass a request object
    #Pass data using context dictionary
    context = {
        "title":"Important Information"
    }
    return render(request, "info.html", context=context)