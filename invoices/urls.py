from django.urls import path
from . import views

urlpatterns = [
    path('<int:invoice_id>/pdf/', views.invoice_pdf, name='invoice_pdf'),
]