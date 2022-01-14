from django.shortcuts import render,redirect
from apparel.models import PRODUCTS,CUSTOMERS,ORDERS
from apparel.forms import PRODUCTSForm,CUSTOMERSForm,ORDERSForm

def pdelete(request,id):
    print("id=",id)
    products=PRODUCTS.objects.get(id=id)
    products.delete()
    return redirect('/home') # / represents it goes to home page

'''def cdelete(request,id):
	customers=PRODUCTS.objects.get(id=id)
	products.delete()
	return redirect('/')'''
