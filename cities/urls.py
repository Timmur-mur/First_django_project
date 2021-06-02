from cities.views import CityCreateView, CityDeliteView, CityDetailView, CityUpdateView, home, CityListView
from django.urls import path

urlpatterns = [
    #path('', home, name = 'home'),
    path('', CityListView.as_view(), name = 'home'),
    path('detail/<int:pk>/', CityDetailView.as_view(), name='detail'),
    path('add/', CityCreateView.as_view(), name ='create'),
    path('update/<int:pk>/', CityUpdateView.as_view(), name='update'),
     path('delite/<int:pk>/', CityDeliteView.as_view(), name='delite'),
]