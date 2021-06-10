from django.contrib import admin

# Register your models here.
from trains.models import Train



class TrainAdmin(admin.ModelAdmin):

    class Meta:
        model = Train

    list_display = ['name', 'from_city', 'to_city', 'travel_time']  #позволяет менять отображение в панели админа
    list_editable=['travel_time'] #делает поля в этом списке изменяемыми


admin.site.register(Train, TrainAdmin)