from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from . models import *
from . forms import Arrivalform

# Create your views here.

def home(req):
    return render(req,'home.html')

def women(req):
    return render(req,'women.html')

def wallet(req):
    a=Product.objects.filter(cname='Wwallets')
    return render(req,'wallet.html',{'form':a})

def men(req):
    return render(req,'men.html')

def sample(req):
    return render(req,'sample.html')

def sling(req):
    a=Product.objects.filter(cname='Wslings')
    return render(req,'sling.html',{'form':a})
    
def tote(req):
    a=Product.objects.filter(cname='Wtote')
    return render(req,'tote.html',{'form':a})

def backpack(req):
    a=Product.objects.filter(cname='Wbackpack')
    return render(req,'backpack.html',{'form':a})   

def office(req):
    a=Product.objects.filter(cname='Woffice')
    return render(req,'office.html',{'form':a})

def men(req):
    return render(req,'men.html')

def menoffice(req):
    a=Product.objects.filter(cname='Moffice')
    return render(req,'menoffice.html',{'form':a}) 

def menwallet(req):
    a=Product.objects.filter(cname='Mwallets')
    return render(req,'menwallet.html',{'form':a})  

def detail(req,name):
    data=Product.objects.get(name=name)
    return render(req,'detail.html',{'form':data})

def arrivals(req):
    data=Newarrival.objects.all()
    return  render(req,'newarrivals.html',{'form':data})

def add(req):
    if req.method=='POST':
        form=Arrivalform(req.POST,req.FILES)
        if form.is_valid():
            form.save()
            return redirect(arrivals)
    else:
        form=Arrivalform()
        return render(req,'arrivaladd.html',{'form':form})
def edit(req,id):
    obj1=Newarrival.objects.get(id=id)
    if req.method=='POST':
        form=Arrivalform(req.POST,req.FILES,instance=obj1)
        if form.is_valid():
            form.save()
            return redirect(arrivals)
    else:
        form=Arrivalform(instance=obj1)
        return render(req,'arrivaladd.html',{'form':form})

def remove(req,id):
    obj1=Newarrival.objects.get(id=id)
    obj1.delete()
    return redirect(arrivals)
     
def loginuser(req):
    if req.method=='POST':
        username=req.POST['username']
        password=req.POST['password']
        user=authenticate(req,username=username,password=password)
        if user:
            login(req,user)
            print('succes')
            return redirect(home)
        else:
            print('error')   
    return render(req,'login.html')
