from django.urls import path
from .import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('task-list/', views.taskList, name='api-task-list'),
    path('task-detail/<str:pk>', views.taskDetail, name='api-task-detail'),
    path('task-create/', views.taskCreate, name='api-task-create'),
    path('task-update/<str:pk>', views.taskUpdate, name='api-task-update'),
    path('task-delete/<str:pk>', views.taskDelete, name='api-task-delete'),
]