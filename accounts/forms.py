from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class ClientRegisterForm(UserCreationForm):
    phone_number = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email', 'phone_number',)
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_customer = True
        user.email = self.cleaned_data['email']
        user.phone_number = self.cleaned_data['phone_number']
        if commit:
            user.save()
        return user
