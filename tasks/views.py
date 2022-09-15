from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *

# Create your views here.

def index(request):
    tasks = Task.objects.all() #get all the task objects

    form = TaskForm() #Form object from the forms.py

    if request.method == "POST":  # when user use input new task in the top box, 
        form = TaskForm(request.POST) # the value will be passed into form
        if form.is_valid():
            form.save()
        return redirect('/') # redirect user back to home page, which in this case is the same page

    context = {'tasks': tasks, 'form':form} #A context is a variable name -> variable value mapping that is passed to a template.

    return render(request, 'tasks/list.html', context)

def updateTask(request, pk):
    task = Task.objects.get(id=pk) #notice the task here is not all objects, but the task object of a specific pk
    form = TaskForm(instance=task) #the same object as the one we retrieved above, and TaskForm would pre-fill the form for us. 
    context = {'form':form}

    if request.method == "POST": #if user change the form,
        form = TaskForm(request.POST, instance=task) # let's grab new data, but still with the same instance
        if form.is_valid():
            form.save() # if valid, save
            return redirect('/') # redirect page back to the home page

    return render(request, 'tasks/update_task.html', context)

def deleteTask(request, pk):
    task = Task.objects.get(id=pk)
    context = {'task': task}

    if request.method == "POST":
        task.delete()
        return redirect('/')

    return render(request, 'tasks/delete.html', context)