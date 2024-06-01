from django.contrib import admin
from .models import Task, Label

@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner')
    search_fields = ('name', 'owner__username')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'owner', 'completion_status', 'get_labels')
    search_fields = ('title', 'description', 'owner__username')
    list_filter = ('completion_status', 'labels')
    filter_horizontal = ('labels',)

    def get_labels(self, obj):
        return ", ".join([label.name for label in obj.labels.all()])
    get_labels.short_description = 'Labels'
