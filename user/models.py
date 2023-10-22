from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class CustomUser(AbstractUser):
    STATUSES = (
        ('ACTIVE', 'active'),
        ('BLOCKED', 'blocked'),
    )
    # REQUIRED_FIELDS = []
    # USERNAME_FIELD = 'email'
    first_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    # last_login = models.DateTimeField(auto_now=True)
    # date_joined = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUSES, default="ACTIVE")

    def __str__(self):
        return self.first_name

