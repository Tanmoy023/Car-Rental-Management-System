from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Add any additional fields here
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    is_customer = models.BooleanField(default=True)
    
    def __str__(self):
        return self.username
