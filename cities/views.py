from cities.forms import HtmlForm, CityForm
from django.views.generic.detail import DetailView
from cities.models import City
from django.shortcuts import get_object_or_404, render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.views.generic import ListView
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.


def home(request, pk=None):
    if request.method == 'POST':
        #form = HtmlForm(request.POST)
        form = CityForm(request.POST)
        if form.is_valid(): #проверка соответствия набору полей
            print(form.cleaned_data) #очищенные данные из формы {'name': 'Кишенев'}
            form.save() #сохранение данных из формы в базу соответствующей привязанной модели
#    if pk:

#       city = get_object_or_404(City, id=pk)
        
#        context = {'object': city}
#        return render(request, 'cities/detail.html', context)
    form = CityForm() 
    qs = City.objects.all()

    lis = Paginator(qs, 3)
    page_number = request.GET.get('page') #пагинация разбивка на страницы и задание кол-ва отображений
    page_obj = lis.get_page(page_number)

    context = {'page_obj': page_obj, 'form': form}
    return render(request, 'cities/home.html', context)




class CityDetailView(DetailView):

    queryset = City.objects.all()
    template_name = 'cities/detail.html'


class CityCreateView(SuccessMessageMixin, CreateView):
    
    model = City
    form_class = CityForm
    template_name = 'cities/create.html'
    success_url = reverse_lazy('cities:home') # формирует адрес перехода после создания 
    success_message = 'Город успешно добавлен'


class CityUpdateView(SuccessMessageMixin, UpdateView):
    
    model = City
    form_class = CityForm
    template_name = 'cities/update.html'
    success_url = reverse_lazy('cities:home')
    success_message = 'Город успешно обновлен'


class CityDeliteView(DeleteView):
    
    model = City
    form_class = CityForm
    template_name = 'cities/delite.html' # удаление с подтверждением
    success_url = reverse_lazy('cities:home')


class CityListView(ListView):
    paginate_by = 2
    model = City
    template_name = 'cities/home.html'

    def get_context_data(self, **kwargs): # метод служит для передачи каких то конкретных данных в контекст 
        context = super().get_context_data(**kwargs)
        form = CityForm()
        context['form'] = form # конкретно тут просиходит добавление нового класса формы в контекст отображения списка
        return context
        

