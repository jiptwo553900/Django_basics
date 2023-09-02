from django.shortcuts import render, redirect
from django.views.generic import UpdateView, DeleteView

from .models import Task
from .forms import TaskForm


def todo_list(request):
    tasks = Task.objects.order_by('-date')
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')

    context = {
        'tasks': tasks,
        'form': form
    }
    return render(request, 'todo/list.html', context)


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'todo/update.html'
    form_class = TaskForm


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'todo/delete.html'
    success_url = '/todo'