from django.shortcuts import render

from django.http import HttpResponse

def cse(request):
    return HttpResponse("Welcome on CSE page")

def etc(request):
    return HttpResponse("Welcome on E&TC page")

    
def mech (request):
    return HttpResponse("Welcome to MECH page")

def civil(request):
    return HttpResponse    ("Welcome to CIVIL page")
 