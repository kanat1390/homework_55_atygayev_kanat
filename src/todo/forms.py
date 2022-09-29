from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ['is_deleted', 'deleted_at']
        labels = {
            'title':'',
            'description':'',
            'status':'',
            'date_due':'',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Название задачи'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Название задачи'}),
            'status': forms.Select(attrs={'class': 'form-control form-control-custom'}),
            'date_due': forms.TextInput(attrs={'class': 'form-control  form-control-custom', 'placeholder':'day/month/year'}),
        }