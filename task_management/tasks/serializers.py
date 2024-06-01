from rest_framework import serializers
from .models import Task, Label

class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        #fields = '__all__'
        fields = ['id', 'name']

class TaskSerializer(serializers.ModelSerializer):
    labels = LabelSerializer(many=True, read_only=True)
    class Meta:
        model = Task
        #fields = '__all__'
        fields = ['id', 'title', 'description', 'completion_status', 'labels']
        
        
        
