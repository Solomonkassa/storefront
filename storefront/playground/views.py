from django.shortcuts import render
from django.http import HttpResponse
from django.db.models.aggregates import Count, Sum, Avg, Max, Min
from django.db.models.functions import Concat
from django.db.models import Value, F, Func
from store.models import Product, Customer




def SayHello(request):
    
    query_set = Customer.objects.annotate(
        fullname = Concat(('first_name'),Value(' '),('last_name'))
    )
        
    return render(request,'hello.html', {'Customers': list(query_set) })


    