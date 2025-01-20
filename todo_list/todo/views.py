from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from todo.models import TaskQuestions
from todo.forms import TaskForm


def home_view(request):
    return render(request, 'html/home.html')


@login_required
def todo_list_view(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('todo_list')
    else:
        form = TaskForm()

    tasks = TaskQuestions.objects.filter(user=request.user)
    return render(request, 'html/todo_list.html', {'form': form, 'tasks': tasks})
