from django.urls import path
from .views import task_list, task_detail, task_delete, task_delete_confirm, task_create
urlpatterns = [
    path('', task_list, name='task-list'),
    path('tasks/<int:pk>/', task_detail, name='task-detail'),
    path('tasks/<int:pk>/delete/', task_delete, name='task-delete'),
    path('tasks/<int:pk>/delete/confirm/', task_delete_confirm, name='task-delete-confirm'),
    path('tasks/create/', task_create, name='task-create'),
]
