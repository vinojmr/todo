from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Todo
from .forms import Todoform
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView
# Create your views here.


class Update(UpdateView):
    model = Todo
    template_name = 'edit.html'
    context_object_name = 'edit'
    fields = ('name', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('detail', kwargs ={'pk': self.object.id})


class Delete(DeleteView):
    model = Todo
    template_name = 'delete.html'
    success_url = reverse_lazy('index')


class List(ListView):
    model = Todo
    template_name = 'home.html'
    context_object_name = 'lists'


class Detail(DetailView):
    model = Todo
    template_name = 'detail.html'
    context_object_name = 'details'


def index(req):
    tasks = Todo.objects.all()
    if req.method == 'POST':
        name = req.POST.get('task',)
        prior = req.POST.get('priority',)
        date = req.POST.get('date',)
        task = Todo(name=name, priority=prior, date=date)
        task.save()
    return render(req, 'index.html', {'tasks': tasks})


def details(req):
    task = Todo.objects.all()
    return render(req, 'details.html', {'task': task})


def delete(req, id):
    delete = Todo.objects.get(id=id)
    if req.method == 'POST':
        delete.delete()
        return redirect('/')
    return render(req, 'delete.html')


def update(req, id):
    task_update = Todo.objects.get(id=id)
    f = Todoform(req.POST or None, instance=task_update)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(req, 'update.html', {'f': f})

