from django.db import models

STATUS_CHOICES = [
    ('N', 'Новая'),
    ('C', 'Выполнена')
]

class Task(models.Model):
    title = models.CharField(null=False, blank=False, max_length=40)
    description = models.TextField(null=True, blank=True, max_length=500)
    status = models.CharField(choices=STATUS_CHOICES, max_length=1, null=False, blank=False)
    date_due = models.DateField(null=True, blank=True, default=None)
    deleted_at = models.DateTimeField(null=True, blank=True, default=None)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title

