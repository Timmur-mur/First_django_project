from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from trains.forms import TrainForm
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from trains.models import Train


class TrainListView(ListView):
    paginate_by = 5
    model = Train
    template_name = 'trains/trains.html'


class TrainDetailView(DetailView):

    model = Train
    template_name = 'trains/detail.html'


class TrainCreateView(SuccessMessageMixin, CreateView):
    
    model = Train
    form_class = TrainForm
    template_name = 'trains/create.html'
    success_url = reverse_lazy('trains:trains') # формирует адрес перехода после создания 
    success_message = 'Поезд успешно добавлен'


class TrainUpdateView(SuccessMessageMixin, UpdateView):
    
    model = Train
    form_class = TrainForm
    template_name = 'trains/update.html'
    success_url = reverse_lazy('trains:trains')
    success_message = 'Поезд успешно обновлен'


class TrainDeliteView(DeleteView):
    
    model = Train
    form_class = TrainForm
    template_name = 'trains/delite.html' # удаление с подтверждением
    success_url = reverse_lazy('trains:trains')
