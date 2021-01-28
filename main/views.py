from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from .models import Bill
from .forms import *
from .functions.functions import *
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
def add(request):

    if request.method == 'POST':
        addForm = AddForm(request.POST,request.FILES)
        if addForm.is_valid():
            data = addForm.cleaned_data
            bill = Bill()
            
            bill.setF(data['money'],data['date'])
            bill.image = request.FILES['image']
            bill.url_image = bill.image.url
            if len(Bill.objects.filter(url_image=bill.url_image)):
                return HttpResponse("Image is exist")
            #handle_uploaded_file(request.FILES['image'])
            bill.save()
        return HttpResponseRedirect(reverse('main:home'))

    form = AddForm()
    return render(request,'app/add.html',{
        'form':form
    })
