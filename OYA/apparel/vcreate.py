from django.shortcuts import render,redirect
from apparel.models import PRODUCTS,CUSTOMERS,ORDERS
from apparel.forms import PRODUCTSForm,CUSTOMERSForm,ORDERSForm

def pcreate(request):
    form=PRODUCTSForm()
    if request.method=='POST':
        form=PRODUCTSForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'create/pcreate.html',{'form':form})

def ccreate(request):
    form=CUSTOMERSForm()
    if request.method=='POST':
        form=CUSTOMERSForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'create/ccreate.html',{'form':form})

def ocreate(request):
    form=ORDERSForm()
    if request.method=='POST':
        form=ORDERSForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'create/ocreate.html',{'form':form})
