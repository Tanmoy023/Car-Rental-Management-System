from django.urls import path
from .views import CarListView, CarDetailView, HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('cars/', CarListView.as_view(), name='car_list'),
    path('cars/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
]
