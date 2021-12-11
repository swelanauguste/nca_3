from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView

from .models import Payment
from .forms import PaymentCreateForm, PaymentUpdateForm


class PaymentListView(ListView):
    model = Payment


class PaymentDetailView(DetailView):
    model = Payment


class PaymentUpdateView(UpdateView):
    model = Payment
    form_class = PaymentUpdateForm


class PaymentCreateView(CreateView):
    model = Payment
    form_class = PaymentCreateForm
