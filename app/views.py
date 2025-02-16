from django.shortcuts import render,redirect
from .forms import *
from .models import *

# Create your views here.

def matrimonyView(request):
    fm=MatrimonyForm()
    if request.method=='POST':
        fm=MatrimonyForm(request.POST)
        if fm.is_valid():
            cleaned_data=fm.cleaned_data
            MatrimonyModel.objects.create(**cleaned_data)
            return redirect('unmarried')
        

            
            
    return render(request, 'matrimony.html',{'form':fm})

def unmarried(request):
    users=MatrimonyModel.objects.all()
    return render(request, 'unmarried.html',{'users':users})

def update(request,id):
    user=MatrimonyModel.objects.get(id=id)
    fm=MatrimonyForm()
    if request.method=='POST':
        fm=MatrimonyForm(request.POST)
        if fm.is_valid():
            all_data=fm.cleaned_data
            MatrimonyModel.objects.update(**all_data)
            return redirect('unmarried')
    return render(request, 'update.html',{'form':fm,'user':user})

def delete(request,id):
    MatrimonyModel.objects.filter(id=id).delete()
    return redirect('unmarried')

def user(request):
    query=request.GET.get('st','')
    user=MatrimonyModel.objects.filter(name__icontains=query)
    return render(request, 'user.html',{'user':user})