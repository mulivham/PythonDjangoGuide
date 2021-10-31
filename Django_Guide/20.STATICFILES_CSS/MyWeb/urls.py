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
from django.urls import path

#from . import views # (.)If the views is from the same directory

#Example 1

#from . import views
from Page import views

urlpatterns = [
    path('admin/', admin.site.urls),

    #My own added path

    path('', views.HomeView, name="home"),
    path('info/', views.info_page, name="information"),
    
    path('contact/', views.conTactPaGe, name="contact"),
    
    path('create/', views.create_post, name="create-post"),
    path('list/', views.list_of_posts, name="post-list"),

    path('community/<int:post_id>/', views.Community_Page, name="post-issue"),
    path('community/<int:post_id>/delete/',views.delete_post, name="delete-post"),
    path('community/<int:post_id>/update/',views.update_post, name="update-post"),
]

#OPTION 1

#+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#OPTION 2

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#OPTION 3

"""
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
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