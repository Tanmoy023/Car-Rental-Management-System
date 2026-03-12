from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic import CreateView
from .forms import ClientRegisterForm # We need to create this form
from django.urls import reverse_lazy

class RegisterView(CreateView):
    template_name = 'accounts/register.html'
    form_class = ClientRegisterForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.success_url)
