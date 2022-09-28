from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    exclude = ('deleted_at', 'is_deleted')


admin.site.register(Task, TaskAdmin)


