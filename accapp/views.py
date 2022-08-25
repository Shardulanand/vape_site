
from itertools import product
from multiprocessing import context
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from accapp.forms import *
from .models import *

app_name='accapp'



def home(request):
    return render(request,'accapp/home.html')



def createuser(request):                                                                              
    if request.method =="POST":
        form= UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account Created Successfully!!')
            return redirect('accapp:myloginurl')
        else:
            print(form.errors)
            messages.error(request,'Something Went Wrong')
            return redirect('accapp:registerurl')
    return render(request,'accapp/Createuser.html')



def mylogin(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user= authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'Logged In Successfully!!')
            return redirect('accapp:homeurl')
        else:
            messages.error(request,'Something Went Wrong')
            return redirect('accapp:myloginurl')
    return render(request,'accapp/login.html')

def mylogout(request):
    logout(request)
    messages.success(request,'Logged Out Successfully!!')
    return redirect('accapp:homeurl')

def addproduct(request):
    if request.method == 'POST':
        form=product_Form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
        return redirect("accapp:cataloglisturl")
    form=product_Form()
    context={
        'form':form,
    }
    return render(request,'accapp/catalog.html',context)

def listproduct(request):
    productInst= product.objects.all()
    context={
        'productInst':productInst,
    }
    return render(request,'accapp/cataloglist.html',context)

def contact(request):
    if request.method == 'POST':
        form=reachus_Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Your Query Has been Succesfully delivered!! Our team will contact you soon')
        else:
            print(form.errors)
        return redirect('accapp:homeurl') 
    form=reachus_Form()
    context={
        'form':form,
    }
    return render(request,'accapp/home.html',context)
   


