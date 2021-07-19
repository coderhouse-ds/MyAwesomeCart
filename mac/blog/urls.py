from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="BlogsHome"),
    path("blogpost/", views.blog, name="blogPost")
]