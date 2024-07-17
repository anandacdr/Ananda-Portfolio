from django.urls import path
from . import views

# localhost:8000/blogs

urlpatterns = [
    path('', views.all_blogs, name='all_blogs')
]
