from django.urls import path

from . import views

app_name = "payments"


urlpatterns = [
    path("", views.PaymentListView.as_view(), name="payment-list"),
    path("new", views.PaymentCreateView.as_view(), name="payment-create"),
    path(
        "detail-<slug:slug>", views.PaymentDetailView.as_view(), name="payment-detail"
    ),
    path(
        "update-<slug:slug>", views.PaymentUpdateView.as_view(), name="payment-update"
    ),
]
