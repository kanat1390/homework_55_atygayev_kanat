from django.shortcuts import render

def task_list(request):
    context = {}
    return render(request, 'todo/task_list.html', context)
