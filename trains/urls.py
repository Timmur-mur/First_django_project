from trains.views import TrainCreateView, TrainDeliteView, TrainDetailView, TrainListView, TrainUpdateView
from django.urls import path

urlpatterns = [
    #path('', home, name = 'home'),
    path('', TrainListView.as_view(), name = 'trains'),
    path('detail/<int:pk>/', TrainDetailView.as_view(), name = 'detail'),
    path('add/', TrainCreateView.as_view(), name ='create'),
    path('update/<int:pk>/', TrainUpdateView.as_view(), name='update'),
    path('delite/<int:pk>/', TrainDeliteView.as_view(), name='delite'),

]