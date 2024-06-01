 # This file contains the database models for the app

from django.db import models
from django.contrib.auth.models import User # Django’s User for authentication
from django.urls import reverse # To give us greater flexibility with creating URLs


# Creating label model 
# on_delete=models.CASCADE specifies that if the user associated with a label is deleted, all labels associated with that user will also be deleted.
    
class Label(models.Model):
    name = models.CharField(max_length=100, unique=True)
    owner = models.ForeignKey(User, related_name='labels', on_delete=models.CASCADE) # The related_name parameter allows to access labels associated with a user via the user object. 
    
    # This creates a unique constraint on the combination of the owner and name fields. It ensures that each user unique name.
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["owner", "name"], name="owner_name")
        ]
    
    def __str__(self):
        return self.name

# Creating task model 
class Task(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    completion_status = models.BooleanField(default=False)
    owner = models.ForeignKey(User, related_name='tasks', on_delete= models.CASCADE)
    labels = models.ManyToManyField(Label, related_name='tasks')
    

    # This part specifies a unique constraint on the combination of the owner and title fields. It ensures that each user can have only one task with a given title.
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["owner", "title"], name="owner_title")
        ]
    
    def __str__(self):
        return self.title

