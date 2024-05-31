from django.db import models
from django.contrib.auth.models import User # Django’s User for authentication
from django.urls import reverse # To give us greater flexibility with creating URLs


# Creating label model here
class Label(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class Meta:
    unique_togther = ('name', 'owner')

def __str__(self):
    return self.name

# Creating task model here
class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    completion_status = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete= models.CASCADE)
    labels = models.ManyToManyField(Label, related_name='tasks')
    
def __str__(self):
    return self.title