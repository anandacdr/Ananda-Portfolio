from django.shortcuts import render
from .models import BlogsTypes

# Create your views here.
def all_blogs(request):
    # Declare a variable to show data in front-end
    blogs = BlogsTypes.objects.all
    
    return render (request, 'blogs/all_blogs.html')