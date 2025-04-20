from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    
    def __str__(self):
        return self.title

class Link(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='links')
    url = models.URLField()
    name = models.CharField(max_length=150)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    