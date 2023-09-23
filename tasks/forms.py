from django import forms
from .models import Task
from django.forms.widgets import DateTimeInput


class TaskCreationForm(forms.ModelForm):

    priority = forms.ChoiceField(choices=Task.PRIORITY_CHOICES, initial=1)

    class Meta:
        model = Task
        fields = ['title', 'description', 'priority', 'due_date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['due_date'].widget = DateTimeInput(attrs={'type': 'datetime-local'})


class TaskUpdateForm(TaskCreationForm):

    class Meta:
        model = Task
        fields = ['title', 'description', 'priority', 'due_date', 'completed']
