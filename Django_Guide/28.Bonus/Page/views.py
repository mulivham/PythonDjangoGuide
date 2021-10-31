from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.http import HttpResponse

# Create your views here.

from .models import Page

from django.contrib.auth.mixins import LoginRequiredMixin

#Class Based Module import
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	TemplateView,
	UpdateView,
	DeleteView,
	View
)

from .forms import PageForm, CustomUserCreationForm


class SignupView(CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm #UserCreationForms

#OPTION 1

#    success_url ='/login/'

#OPTION 2
    def get_success_url(self):
        return reverse("login")
"""
#OPTION 3
    def get_success_url(self):
        return "/login/"
#-------------------------------
from django.contrib.auth.forms import UserCreationForm

class SignupView(CreateView):
    template_name = "registration/signup.html"
    form_class = UserCreationForm

#OPTION 1

    success_url ='/login/'

#OPTION 2
    def get_success_url(self):
        return reverse("login")

#OPTION 3
    def get_success_url(self):
        return "/login/"


"""
#---------------- Update Example -----------------
#Class Bases View
class update_post(UpdateView):
	template_name = "Forms/create_post.html"
	form_class = PageForm
	queryset = Page.objects.all()
	
	success_url ='/community/'

	#def get_success_url(self):
		#return'/list/'

"""     -----------------------
def update_post(request, post_id):
	obj = Page.objects.get(id=post_id)
	form = PageForm(instance=obj)

	if request.method == "POST":
		form = PageForm(request.POST, request.FILES or None,instance=obj)
	if form.is_valid():
		image = request.FILES['image']
		form.image = image
		form.save()
		return redirect('../../../list/')

	context = {
		'form' : form
	}
	return render(request, 'Forms/create_post.html', context)
	
"""
#--------------- Delete Example ---------------
#Class Based View

class delete_post(DeleteView):
	template_name = "Forms/delete_post.html"
	queryset = Page.objects.all()
	success_url ='/community/'

	#def get_success_url(self):
		#return'/list/'

"""       -----------------------
def delete_post(request,post_id): 
	obj = get_object_or_404( Page, id=post_id)
	
	if request.method == "POST":
		obj.delete()
		return redirect('../../../list/')
	context = {
		'object':obj
	}
	return render(request,"Forms/delete_post.html", context)
	
"""
#------------------- Page Home ---------------
#Class Based View

class Community_Page(DetailView):
	template_name = "community.html"
	queryset = Page.objects.all()

""" -----------------------
def Community_Page(request, post_id):
	obj = Page.objects.get(id=post_id)
	context ={
		'object' : obj #in Html include object(title.object)
	}
	return render(request,'community.html',context)

"""
#------ Example of List of posts(object) ------------

#Class Based View

from django.contrib.auth.mixins import LoginRequiredMixin

class list_of_posts(LoginRequiredMixin, ListView):
	template_name = "Forms/post_list.html"
	queryset = Page.objects.all()
 
"""# Course/Raw Based View
class list_of_posts(View):
	template_name = "Forms/post_list.html"
	queryset = Page.objects.all()

	def get(self, request, *args, **kwargs):
		context = {
		'object_list' : self.queryset
		}
		return render(request, self.template_name, context)"""

"""
def list_of_posts(request):
	queryset = Page.objects.all()
	context = {
		'object_list' : queryset
	}
	return render(request, 'Forms/post_list.html', context)

"""
#----------------- Form Example ----------------------
#Class Based View/ Direct Generic example

from django.views import generic

class create_post(LoginRequiredMixin,generic.CreateView): #Direct Generic example
	template_name = "Forms/create_post.html"
	form_class = PageForm
	queryset = Page.objects.all()
	
	#success_url ='/list/'

	def get_success_url(self):
		return '/community/'

"""------------------

def create_post(request):
	form = PageForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		image = request.FILES['image']
		form.image = image
		form.save()
		form = PageForm()
		return redirect('../../../list/')

	context = {
		'form' : form
	}
	return render(request, 'Forms/create_post.html', context)

"""
#------------------------------------------------------
#Class Based View

class HomeView(TemplateView):
	template_name = "home.html"

""" --------
def HomeView(request): 
    #return HttpResponse('Welcome To My Home')
    #return HttpResponse('<h1>Welcome To My Home</h1>') # <h1></h1> is html language
    return render(request,'home.html',{}) # {} is the context
    
"""
# ----------- Context Example ------------------------
# Course/Raw Based View

class conTactPaGe(View):
	template_name = "contact.html"

	def get(self, request, *args, **kwargs):
		my_context = {
			"email_address" : "Email : jeancollins.mulivha@gmail.com ",
			"my_number" : " Cell No : +27 66 4472 000 ",
			'social_media' : 'Twitter : @jc_le_mulivha'
		}
		return render(request, self.template_name, my_context)

""" ---------
#Class Based View

class conTactPaGe(TemplateView):
	template_name = "contact.html"

"""
"""
	def conTactPaGe(request):
		my_context = {
			"email_address" : "Email : jeancollins.mulivha@gmail.com ",
			"my_number" : " Cell No : +27 66 4472 000 ",
			'social_media' : 'Twitter : @jc_le_mulivha'
		}
		return render(request,'contact.html',my_context)
	
	"""	
#------------------------ info -----------------------------

#OPTION 1 : Class Based View
"""
class info_page(TemplateView):
	template_name = "info.html"

"""
#OPTION 2 : Course/Raw Based View
class info_page(View):
	template_name = 'info.html'
	def get(self, request, *args, **kwargs):
		return render( request, self.template_name, {})

#OPTION 3 : Def Based View
"""
def info_page(request): 
    return render(request,'info.html',{})

"""
