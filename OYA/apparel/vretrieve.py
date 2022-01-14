from django.shortcuts import render,redirect

from apparel.models import PRODUCTS
from apparel.forms import PRODUCTSForm

def pretrieve(request): # display all objects
	products1=PRODUCTS.objects.all()
	#print(products1.id)
	return render(request,'retrieve/pretrieve.html',{'products':products1})

from apparel.models import ORDERS
from apparel.forms import ORDERSForm

def oretrieve(request): # display all objects
	orders1=ORDERS.objects.all()
	return render(request,'retrieve/oretrieve.html',{'orders':orders1})

from apparel.models import CUSTOMERS
from apparel.forms import CUSTOMERSForm

def cretrieve(request): # display all objects
	customer1=CUSTOMERS.objects.all()
	return render(request,'retrieve/cretrieve.html',{'customer':customer1})
