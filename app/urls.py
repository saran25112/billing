from django.urls import path
from . import views

urlpatterns = [
    path('', views.billing_page, name='billing_page'),
     path('billing-success/', views.billing_success, name='billing_success'),
]
