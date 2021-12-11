from django.contrib.auth.models import AbstractUser
from django.db import models
# from django.urls import reverse
# from django.utils.text import slugify


class User(AbstractUser):
    is_data_entry_clerk = models.BooleanField(default=True)
    is_accountant = models.BooleanField("is the accountant", default=False)
    is_manager = models.BooleanField(default=False)
    is_developer = models.BooleanField(default=False)
    