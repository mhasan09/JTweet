from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [

    path('',tweet_list_view,name="list"),
    path('detail',tweet_detail_view,name="detail")

]
