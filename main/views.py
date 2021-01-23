from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Bill
# Create your views here.
def home(request):
    
    listBill = list(Bill.objects.all())
    sorted(listBill, key=lambda d: d.id,reverse=True)
    
    t = int(sum(int(m.money) for m in listBill))
    s = int((t*60000)//22765000)
    total = t
    salary = s
    return render(request,'app/body.html',{
        'bills':listBill,
        'total':total,
        'salary':salary
    })

