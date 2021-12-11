from django.urls import path

from . import views


app_name = "clients"


urlpatterns = [
    path("", views.ClientListView.as_view(), name="client-list"),
    path("detail-<slug:slug>", views.ClientDetailView.as_view(), name="client-detail"),
    path("update-<slug:slug>", views.ClientUpdateView.as_view(), name="client-update"),
    path("new", views.ClientCreateView.as_view(), name="client-create"),
]
