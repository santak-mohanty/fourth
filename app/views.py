from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def santak(request):
    return HttpResponse("<marquee><h1>My name is Santak</h1></marquee>")
 
