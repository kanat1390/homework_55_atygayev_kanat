from django.urls import reverse
from django.shortcuts import render, redirect
from todo.services import task_service
from .forms import TaskForm

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

def task_delete(request, pk):
    task = task_service.get_task_by_pk(pk)
    context = {
        'task': task,
    }
    return render(request, 'todo/task_delete.html', context)

def task_delete_confirm(request, pk):
    task_service.soft_delete_by_pk(pk)
    return redirect('task-list')


def task_create(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('task-list')
    context = {
        'form': form,
    }
    return render(request, 'todo/task_create.html', context)

def task_update(request, pk):
    task = task_service.get_task_by_pk(pk)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect(reverse('task-detail', kwargs={'pk':task.id}))
    context = {
        'form': form,
    }
    return render(request, 'todo/task_update.html', context)


