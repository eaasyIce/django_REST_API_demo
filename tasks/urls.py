from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='list'),
    path('update_task/<str:pk>/', views.updateTask, name="update_task"), #The string contain angle brackets (like <str:pk>) to capture part of the URL and send it as a keyword argument to the view. 
    # see https://docs.djangoproject.com/en/4.1/ref/urls/
    path('delete/<str:pk>/', views.deleteTask, name="delete")

]
