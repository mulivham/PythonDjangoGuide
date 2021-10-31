"""MyWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
#from django.urls import include, path

#from . import views # (.)If the views is from the same directory

#Example 1

#For My staticFiles
from django.conf import settings
from django.conf.urls.static import static

#from . import views

from django.urls import include, path
from Page import views

from django.contrib.auth.views import (
    LoginView, 
    LogoutView, 
)

from Page.views import HomeView, info_page, conTactPaGe, SignupView

urlpatterns = [
    
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    #Importing Url From Page Folder/App
    path('community/', include('Page.urls')), 
    path('admin/', admin.site.urls),

    #My own added path
    path('', HomeView.as_view(), name="home"),
    path('info/', info_page.as_view(), name="information"),
    path('contact/', conTactPaGe.as_view(), name="contact"),
]

#OPTION 1

#+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#OPTION 2

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#OPTION 3

"""
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"""

#OR
#Example 2 

"""
from Page.views import HomeView, info_page, Community_Page, conTactPaGe

urlpatterns = [
    path('admin/', admin.site.urls),

    #My own added path

    path('', HomeView,),
    path('info/', info_page, ),
    path('community/',Community_Page),
    path('contact/', conTactPaGe),
]
"""
