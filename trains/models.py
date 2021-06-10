from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.deletion import CASCADE
from cities.models import City


# Create your models here.

class Train(models.Model):
    name= models.CharField(max_length=80, unique=True,
                            verbose_name='Номер поезда')
    travel_time = models.PositiveSmallIntegerField(verbose_name='Время в пути')

    from_city = models.ForeignKey(City, on_delete=CASCADE,
                                related_name='from_city_set',
                                verbose_name='Из какого города')
    to_city = models.ForeignKey(City, on_delete=CASCADE,
                                related_name='to_city_set',
                                verbose_name='В какой город')

    def __str__(self):
        return f'Поезд N{self.name} из города {self.from_city}'


    class Meta: #класс для отображения внутри админ панели
        verbose_name = 'Поезд'
        verbose_name_plural = 'Поезда'
        ordering = ['travel_time']


    def clean(self):
        if self.from_city == self.to_city:
            raise ValidationError('Совпадают города отправления и назначения')

        qs = self.__class__.objects.filter(from_city = self.from_city, # выборка элементов из базы что бы распознать дубликат
                                        to_city = self.to_city,
                                        travel_time = self.travel_time).exclude(pk = self.pk) # метод исключает из выборки запись в базе которая уже создана по этому ей присвоен pk
        if qs.exists(): #метод проверяет наличие хотя бы одного элемента в списке
            raise ValidationError ('Запись с такими параметрами уже существует')


    def save(self, *args, **kwargs):
        self.clean()
        super().save(args, **kwargs)