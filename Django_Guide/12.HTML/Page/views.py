from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def HomeView(request): 
    #return HttpResponse('Welcome To My Home')
    #return HttpResponse('<h1>Welcome To My Home</h1>') # <h1></h1> is html language
    return render(request,'home.html',{}) # {} is the context

def info_page(request): 
    return render(request,'info.html',{})

def Community_Page(request):
    return render(request,'community.html',{})

def conTactPaGe(request): 
    return render(request,'contact.html',{})
    