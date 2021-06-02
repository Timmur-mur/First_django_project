
from django.forms import fields
from cities.models import City
from django import forms


class HtmlForm(forms.Form):
    name = forms.CharField(label='Город') #использование формы не связанной с моделью


class CityForm(forms.ModelForm): # форма привязывается к модели
    name = forms.CharField(label='Город', widget=forms.TextInput(attrs={ # влияние на отрисовку формы
        'class': "form-control",
        'placeholder': 'Введите название города'
        }))

    class Meta:
        model = City
        fields = ('name',) # поля из модели


