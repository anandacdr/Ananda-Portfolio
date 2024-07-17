from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse ("<h1>Welcome to my Portfolio</h2>")
    return render (request, 'webpages/index.html')

