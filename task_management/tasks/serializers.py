# Serializers are used to convert complex data types, such as Django model instances, into native Python datatypes that can then be easily rendered into JSON, XML, or other content types.

from rest_framework import serializers
from .models import Task, Label

# Label model as the model to serialize.
class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = '__all__'
        read_only_fields = ['owner']
        


# Task model as the model to serialize.
class TaskSerializer(serializers.ModelSerializer):
    labels = LabelSerializer(many=True, read_only=True) # Nested serializer for the labels
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['owner']
        

        
        
