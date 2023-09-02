from django.forms import ModelForm, TextInput, CheckboxInput
from .models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Add new task'
            }),

            'is_complete': CheckboxInput(attrs={
                #'class': 'form-control',
                'placeholder': 'Add new task'
            }),
        }