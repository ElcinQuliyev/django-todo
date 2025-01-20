from django import forms
from .models import TaskQuestions


class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskQuestions
        fields = ['title', 'description', 'reward_type']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring focus:ring-purple-500 text-[#374151]',
                'placeholder': 'Enter task title',
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring focus:ring-purple-500 text-[#374151]',
                'placeholder': 'Enter task description',
                'rows': 4,
            }),
            'reward_type': forms.Select(attrs={
                'class': "w-full bg-zinc-700 rounded-lg p-2 text-white border border-gray-600 focus:border-purple-500 focus:ring-2 focus:ring-purple-500 focus:outline-none transition-all duration-300",
            }),
        }
