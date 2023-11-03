from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count, Sum, Q

from .models import Customers
from purchase.models import Purchase


# Create your views here.
def query_customers(request):
    # get all customers
    all_customers = Customers.objects.all()
    # count how many customers have added their age
    """aggregate function basically accept multiple query , perform the 
    intended operation on it and return single value."""
    customers_age = Customers.objects.values("age").aggregate(Count("age"))
    # add the ages of all the customers and return me sum of it
    customers_age = Customers.objects.values("age").aggregate(Sum("age"))

    """For or, and and not we use Q objects in django."""
    cust_name = Customers.objects.filter(
        Q(name__startswith="I") | Q(name__startswith="N")
    )

    # order by age, - represent descending order
    customer_ordering = Customers.objects.order_by("-age")

    """purchases - is the relative_name of Purchase model, it let Customer(parent) model to access
    the fields"""
    add_purchase_amount = Customers.objects.aggregate(Sum("purchases__amount"))
    print(add_purchase_amount)

    return HttpResponse("main")
