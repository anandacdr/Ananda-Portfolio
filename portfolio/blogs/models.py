from django.db import models
from django.utils import timezone

# Create your models here.
class BlogsTypes(models.Model):
    BLOG_TYPES = [
        ('Tech', 'Technology'),
        ('Dev', 'Development'),
        ('Fin', 'Finance'),
        ('AI', 'Artificial Intelligence'),
        ('GD', 'Graphic Designing'),
        ('GD', 'Game Development'),
    ]

    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blog_imgs/')
    date_added = models.DateTimeField(default=timezone.now)
    body = models.CharField(max_length=10000)

    type = models.CharField(max_length=4, choices=BLOG_TYPES)


    def ___str__(self):
        return self.name

