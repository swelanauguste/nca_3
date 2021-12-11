from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView

from .models import Client
from .forms import ClientCreateForm, ClientUpdateForm


class ClientListView(ListView):
    model = Client


class ClientDetailView(DetailView):
    model = Client


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientCreateForm


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientUpdateForm
