from django.shortcuts import render
from todo.services import task_service

def task_list(request):
    task_list = task_service.get_task_list()
    context = {
        'task_list': task_list,
    }
    return render(request, 'todo/task_list.html', context)

def task_detail(request, pk):
    task = task_service.get_task_by_pk(pk)
    context = {
        'task': task,
    }
    return render(request, 'todo/task_detail.html', context)

