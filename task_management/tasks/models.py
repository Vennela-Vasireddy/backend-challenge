from django.db import models
from django.contrib.auth.models import User # Django’s User for authentication
from django.urls import reverse # To give us greater flexibility with creating URLs


# Creating label model here
class Label(models.Model):
    name = models.CharField(max_length=100, unique=True)
    owner = models.ForeignKey(User, related_name='labels', on_delete=models.CASCADE)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["owner", "name"], name="owner_name")
        ]
    
    def __str__(self):
        return self.name

# Creating task model here
class Task(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    completion_status = models.BooleanField(default=False)
    owner = models.ForeignKey(User, related_name='tasks', on_delete= models.CASCADE)
    labels = models.ManyToManyField(Label, related_name='tasks')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["owner", "title"], name="owner_title")
        ]
    
    def __str__(self):
        return self.title

