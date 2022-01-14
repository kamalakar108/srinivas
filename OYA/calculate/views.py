from django.shortcuts import render
from calculate.models import maths
from calculate.forms import mathsForm
# Create your views here.

def calc(request):
        form=mathsForm()
        if request.method=='POST':
            form=mathsForm(request.POST)
            if form.is_valid():
                 price= form.cleaned_data.get("price")
                 number= form.cleaned_data.get("number")
                 Total=price*number
            return render(request,'output.html',{'number':number,'price':price,'Total':Total})
        return render(request,'input.html',{'form':form})
