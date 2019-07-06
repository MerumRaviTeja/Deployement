from django.shortcuts import render
from django.http import HttpResponse
from two.forms import *
def name_view(request):
        form=NameForm()
        return render(request,'name.html',{'form':form})
def age_view(request):
         name=request.GET['name']
         request.session['name']=name
         form=AgeForm()
         return render(request,'age.html',{'form':form})
def gf_view(request):
         age=request.GET['age']
         request.session['age']=age
         form=GFForm()
  
         return render(request,'gf.html',{'form':form})
def results_view(request):
         gf=request.GET['gf']
         request.session['gf']=gf
         return render(request,'results.html')