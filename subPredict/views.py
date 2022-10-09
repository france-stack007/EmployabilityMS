from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_view(request):
    return render(request, "index.html")

def start_view(request):
    return render(request, "start.html")

def end_view(request):
    return render(request, "end.html")
