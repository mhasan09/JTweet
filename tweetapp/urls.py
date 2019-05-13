from django.contrib import admin
from django.urls import path
from .views import ListView, DetailView
urlpatterns = [

    path('', ListView.as_view(), name="list"),
    path('1/', DetailView.as_view(), name="detail")

]
