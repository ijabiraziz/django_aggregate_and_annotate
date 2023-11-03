from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count, Sum, Q

from .models import Customers
# Create your views here.
def query_customers(request):
    all_customers = Customers.objects.all()
    customers_age = Customers.objects.values('age').aggregate(Count('age'))
    customers_age = Customers.objects.values('age').aggregate(Sum('age'))

    cust_name = Customers.objects.filter(Q(name__startswith='I') | Q(name__startswith='N'))

    print(cust_name)

    return HttpResponse('main')

