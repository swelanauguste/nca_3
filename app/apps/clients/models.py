import datetime

from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class Client(models.Model):
    """
    Model for clients.
    """

    GENDER_LIST = [
        ("F", "F"),
        ("M", "M"),
    ]
    client_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_LIST)
    dob = models.DateField("DOB", blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, help_text="Home/Work Phone")
    phone1 = models.CharField("mobile", max_length=10, blank=True)
    nic = models.CharField("NIC", max_length=6, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name + "-" + self.client_id)
        super(Client, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("clients:client-detail", kwargs={"slug": self.slug})

    def get_absolute_update_url(self):
        return reverse("clients:client-update", kwargs={"slug": self.slug})

    def __str__(self):
        return self.name + "(" + self.client_id + ")"
