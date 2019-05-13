from django.shortcuts import render
from .models import Tweet
from django.views.generic import ListView



class TweetListView(ListView):
   template_name = "list_view.html"
   queryset = Tweet.objects.all()





