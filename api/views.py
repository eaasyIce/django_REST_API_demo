from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import status

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from tasks.models import Task

from api import serializers #from anpther app which is task import the models->Task

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'task-list',
        'Detail View':'/task-detail/<str:pk>',
        'Create':'/task-create/',
        'Update':'/task-update/<str:pk>',
        'Delete':'/task-delete/<str:pk>',
    }

    return Response(api_urls)
 
@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
    serializers = TaskSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def taskUpdate(request,pk):
    task = Task.objects.get(id=pk)
    #serializer takes the chosen task instance, but fill with the new data from POST request
    serializers = TaskSerializer(instance=task, data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def taskDelete(request,pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response(status=status.HTTP_200_OK)
