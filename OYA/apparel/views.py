# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

'''










from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from add.models import Employee
from add.forms import EmployeeForm

# Create your views here.
def home(request):
    employee=Employee.objects.filter(esal__gt=500)
    print(employee)
    return render(request,'add.html',{'employee':employee})

def add(request):
    val1=int(request.GET['num1'])
    val2=int(request.GET['num2'])
    result=val1+val2
    return render(request,'add.html',{'result':result})


def create_view(request):
	form=EmployeeForm()
	if request.method=='POST':
		form=EmployeeForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/')
	return render(request,'create.html',{'form':form})

def retrieve_view(request): # display all objects
	employees=Employee.objects.all()
	return render(request,'index.html',{'employees':employees})

def delete_view(request,id):
	employee=Employee.objects.get(id=id)
	employee.delete()
	return redirect('/') # / represents it goes to home page

def update_view(request,id):
	employee=Employee.objects.get(id=id)
	if request.method=='POST':
		form=EmployeeForm(request.POST,instance=employee)
		if form.is_valid():
			form.save()
		return redirect('/')
	return render(request,'update.html',{'employee':employee})
'''
