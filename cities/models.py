from django.db import models
from django.urls import reverse

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Город')

    def __str__(self):
        return self.name

    class Meta: #класс для отображения внутри админ панели
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        ordering = ['name']

    def get_absolute_url(self):# отправляет после создания на детали записи
        return reverse('cities:detail', kwargs={'pk': self.pk})