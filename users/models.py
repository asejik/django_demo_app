from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.

class OKUser(AbstractBaseUser):
    first_name = models.Charfield(max_length=255)
    last_name = models.Charfield(max_length=255)
    is_active = models.BooleanField(default=True)
    is_blocked = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    