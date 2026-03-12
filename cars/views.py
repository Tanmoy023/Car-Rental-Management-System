from django.views.generic import ListView, DetailView, TemplateView
from .models import Car
from django.db.models import Q

class HomeView(TemplateView):
    template_name = 'home.html'

class CarListView(ListView):
    model = Car
    template_name = 'cars/car_list.html'
    context_object_name = 'cars'

    def get_queryset(self):
        queryset = super().get_queryset()
        status = self.request.GET.get('status')
        if status:
            queryset = queryset.filter(status=status)
        else:
            # By default show available and on_rent (maybe just available for booking?)
            # SRS says "Browse available cars".
            pass 
        return queryset

class CarDetailView(DetailView):
    model = Car
    template_name = 'cars/car_detail.html'
    context_object_name = 'car'
