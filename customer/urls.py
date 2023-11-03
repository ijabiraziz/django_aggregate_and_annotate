from django.urls import path
from .views import query_customers

urlpatterns = [
    path('', query_customers),
]
