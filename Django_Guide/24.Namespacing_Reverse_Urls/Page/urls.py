from django.contrib import admin
from django.urls import path
from Page import views

app_name = 'Page'
urlpatterns = [

    path('',views.list_of_posts, name="post-list"),
    path('create/', views.create_post, name="create-post"),
    path('<int:post_id>/',views.Community_Page, name="post-issue"),
    path('<int:post_id>/delete/',views.delete_post, name="delete-post"),
    path('<int:post_id>/update/',views.update_post, name="update-post"),
]