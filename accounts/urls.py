from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    # LogoutView in Django 5.0+ requires POST by default, or separated. 
    # We will use the standard view. The templates handles the POST form.
    path('logout/', LogoutView.as_view(), name='logout'),
]
