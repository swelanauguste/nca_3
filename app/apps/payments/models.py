import uuid

from clients.models import Client
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Payment(models.Model):
    """
    Model for Payments
    """

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(default=0.0, decimal_places=2, max_digits=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.uuid)
        super(Payment, self).save(*args, **kwargs)
        
    def get_absolute_url(self):
        return reverse("payments:payment-detail", kwargs={"slug": self.slug})

    def get_absolute_update_url(self):
        return reverse("payments:payment-update", kwargs={"slug": self.slug})

    def __str__(self):
        return self.client.name + " - $" + str(self.amount)
