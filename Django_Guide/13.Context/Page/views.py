from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def HomeView(request): 
    #return HttpResponse('Welcome To My Home')
    #return HttpResponse('<h1>Welcome To My Home</h1>') # <h1></h1> is html language
    return render(request,'home.html',{}) # {} is the context

# ----------- Context Example ------------------------
def conTactPaGe(request):
	my_context = {
		"email_address" : "Email : jeancollins.mulivha@gmail.com ",
		"my_number" : " Cell No : +27 66 4472 000 ",
		'social_media' : 'Twitter : @jc_le_mulivha'
	}
	return render(request,'contact.html',my_context)
#-------------------------------------------------------
def info_page(request): 
    return render(request,'info.html',{})

def Community_Page(request):
    return render(request,'community.html',{})


    