from django.db import models
from django.db.models.query import QuerySet

STATUS_CHOICES = [
    ('N', 'Новая'),
    ('C', 'Выполнена')
]

class TaskManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(is_deleted = False)

class Task(models.Model):
    title = models.CharField(null=False, blank=False, max_length=40)
    description = models.TextField(null=True, blank=True, max_length=500)
    status = models.CharField(choices=STATUS_CHOICES, max_length=1, null=False, blank=False, default=STATUS_CHOICES[0][0])
    date_due = models.DateField(null=True, blank=True, default=None)
    deleted_at = models.DateTimeField(null=True, blank=True, default=None)
    is_deleted = models.BooleanField(default=False)
    objects = models.Manager()
    tasks = TaskManager()


    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("task-detail", kwargs={"pk": self.pk})
    

    def __str__(self):
        return self.title

