from django.shortcuts import render, reverse, get_object_or_404, redirect

from django.http import HttpResponse


# Create your views here.

from .models import Page

def delete_post(request,post_id): 
	obj = get_object_or_404( Page, id=post_id)
	
	if request.method == "POST":
		obj.delete()
		return redirect('../../../list/')
	context = {
		'object':obj
	}
	return render(request,"Forms/delete_post.html", context)

#----------- Example Dynamic Linking ---------------

def Community_Page(request, post_id):
	obj = Page.objects.get(id=post_id)
	context ={
		'object' : obj #in Html include object(title.object)
	}
	return render(request,'community.html',context)


#------ Example of List of posts(object) ------------

def list_of_posts(request):
	queryset = Page.objects.all()
	context = {
		'object_list' : queryset
	}
	return render(request, 'Forms/post_list.html', context)

#----------------- Form Example ----------------------
from .forms import PageForm

def create_post(request):
	form = PageForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = PageForm()

	context = {
		'form' : form
	}
	return render(request, 'Forms/create_post.html', context)
#------------------------------------------------------

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

#---------- Rendering Database -------------------------
from .models import Page

#Example 1
"""def Community_Page(request):
	obj = Page.objects.get(id=1)
	context ={
		'title' : obj.title,
		"content" : obj.content
	}
	return render(request,'community.html',context)"""

#OR
#Example 2	
"""
 def Community_Page(request):
 	obj = Page.objects.get(id=1)
 	context ={
 		'object' : obj #in Html include object(title.object)
 	}
 	return render(request,'community.html',context)
 """ 