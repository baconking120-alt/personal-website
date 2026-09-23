from django.http import HttpResponse
from django.shortcuts import render

def home_page_view(request):
    return HttpResponse("Homepage")

def about_page_view(request):
    context = {
        "name": "Adam",
        "age": 23,
    }
    return render(request, "pages/about.html", context)