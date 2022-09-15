from dataclasses import field
from rest_framework import serializers
from tasks.models import Task #from anpther app which is task import the models->Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


