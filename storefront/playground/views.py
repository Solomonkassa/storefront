from django.shortcuts import render
from django.http import HttpResponse
<<<<<<< HEAD
from django.db.models.aggregates import Count, Sum, Avg, Max, Min
from django.db.models.functions import Concat
from django.db.models import Value, F, Func
from store.models import Product, Customer




def SayHello(request):
    
    query_set = Customer.objects.annotate(
        fullname = Concat(('first_name'),Value(' '),('last_name'))
    )
        
    return render(request,'hello.html', {'Customers': list(query_set) })
=======
from django.db.models import Value, F, ExpressionWrapper
from django.db import models
from django.contrib.contenttypes.models import ContentType
from store.models import Product, Customer
from tags.models import TaggedItem

def SayHello(request):
   
   content_type = ContentType.objects.get_for_model(Product)
   queryset =TaggedItem.objects.select_related('tag').filter(
       content_type=content_type,
       object_id=1
   )
   return render(request,'hello.html', {'Product': list(queryset)})
>>>>>>> backup-main


    