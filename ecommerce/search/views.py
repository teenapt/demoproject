from django.shortcuts import render
from shop.models import product
from django.db.models import  Q

# Create your views here.
def search(request):
    query=""
    products=None
    if(request.method=="POST"):
        query=request.POST['q']
        if(query):
            products=product.objects.filter(Q(name__icontains=query) | Q(desc__icontains=query))

    return render(request,'search.html',{'query':query,'p':products})
