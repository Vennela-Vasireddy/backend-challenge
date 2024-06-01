# This file contains configurations for Django's admin interface

from django.contrib import admin
from .models import Task, Label # importing Task and Label models from current package


# Registering Label model with admin interface
@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner') # To display 
    search_fields = ('name', 'owner__username') # Can search these fileds


# Registering Task model with admin interface
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'owner', 'completion_status', 'get_labels')
    search_fields = ('title', 'description', 'owner__username')
    list_filter = ('completion_status', 'labels') # To add filters based on completion status and labels
    filter_horizontal = ('labels',) # specifies that the labels field should be displayed with a horizontal filter interface
    
    # To display the name associated with the selected label
    def get_labels(self, obj):
        return ", ".join([label.name for label in obj.labels.all()])
    get_labels.short_description = 'Labels'
