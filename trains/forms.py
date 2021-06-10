
from cities.models import City
from trains.models import Train
from django import forms


class TrainForm(forms.ModelForm): # форма привязывается к модели
    name = forms.CharField(label='Номер поезда', widget=forms.TextInput(attrs={ # влияние на отрисовку формы
                                                'class': "form-control",
                                                'placeholder': 'Введите номер поезда'
                                                }))

    travel_time = forms.IntegerField(label='Время в пути', widget=forms.NumberInput(attrs={ # влияние на отрисовку формы
                                                'class': "form-control",
                                                'placeholder': 'Время в пути'
                                                }))
    from_city = forms.ModelChoiceField(label='Откуда', queryset=City.objects.all(), widget=forms.Select(attrs={
                                                'class': "form-control"
                                                }))

    to_city = forms.ModelChoiceField(label='Куда', queryset=City.objects.all(), widget=forms.Select(attrs={
                                                'class': "form-control"
                                                }))
# связывание формы с классом модели
    class Meta:
        model = Train
        fields = '__all__' 
