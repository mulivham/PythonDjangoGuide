from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def HomeView(request): 
    #return HttpResponse('Welcome To My Home')
    #return HttpResponse('<h1>Welcome To My Home</h1>') # <h1></h1> is html language
    return render(request,'home.html',{}) # {} is the context

def info_page(request): 
    return HttpResponse('Info: This web is all about the communuty')

def Community_Page(request):
    return HttpResponse('Feel free to share and spread the word')

def conTactPaGe(request): 
    #return HttpResponse('email : jeancollins.mulivha@gmail.com')
    return render(request,'contact.html',{})
    