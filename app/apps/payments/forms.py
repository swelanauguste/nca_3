from django import forms

from .models import Payment


class PaymentCreateForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ["client", "amount"]


class PaymentUpdateForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ["client", "amount"]
