from ..models import Task
from django.shortcuts import get_object_or_404
import datetime

def get_task_list():
    return Task.tasks.all()

def get_task_by_pk(pk):
    return get_object_or_404(Task, pk=pk)

def soft_delete_by_pk(pk):
    task = get_object_or_404(Task, pk=pk)
    task.deleted_at = datetime.datetime.now()
    task.is_deleted=True
    task.save()
