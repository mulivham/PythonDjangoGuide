from django.contrib import admin
from django.urls import path
from Page.views import (

    Community_Page,
    update_post,
    delete_post,
    create_post,
    list_of_posts,
)


app_name = 'Page'
urlpatterns = [

    path('',list_of_posts.as_view(), name="post-list"),
    path('create/', create_post.as_view(), name="create-post"),
    path('<int:pk>/',Community_Page.as_view(), name="post-issue"),
    path('<int:pk>/delete/',delete_post.as_view(), name="delete-post"),
    path('<int:slug>/update/',update_post.as_view(), name="update-post"),
]