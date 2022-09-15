from django import forms
from django.forms import ModelForm

from .models import *

class TaskForm(ModelForm):
    class Meta:
        model = Task #using Task object in models.py to build forms
        fields = '__all__' # retrieve all fields from Task: title, completed, created