from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from .models import Bill
from django.db.models import Q
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
            
            bill.setF(data['money'],data['date'],name=data['name'])
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
def search(request):
    
    if request.is_ajax() or request.method == "GET":
        key = request.GET['key']
        if key.isnumeric():
            listBill = list(Bill.objects.filter(money__contains=key))
        else: listBill = list(Bill.objects.filter(Q(name__contains=key)| Q(date__contains=key)))
        content = f"có từ khóa tìm kiếm '{key}'"
        if key == "":
            content = "từ 2/5/2019 đến 30/1/2021"
        sorted(listBill, key=lambda d: d.id,reverse=True)
        return render(request,'app/search.html',{
            'bills':listBill,
            'byMonth':False,
            'content': content
            
        })
    else:
        return HttpResponse("no")
def searchbymonth(request):
    salaryInMonth = totalBill =totalMoney = 0 
    if request.method == "GET":
        key = request.GET['selectVal']
        print(key)
        listBill = list(Bill.objects.filter(date__contains=key))
        sorted(listBill, key=lambda d: d.id,reverse=True)
        content = f"trong tháng {key}"

        totalBill = len(listBill)
        totalMoney = int(sum(int(b.money) for b in listBill))
        salaryInMonth = (totalMoney*60000)//22765000
        return render(request,'app/search.html',{
            'byMonth':True,
            'bills':listBill,
            'content':content,
            'totalMoney': totalMoney,
            'totalBill':totalBill,
            'salaryInMonth':salaryInMonth
        })
    else:
        return HttpResponse("method not allow")
