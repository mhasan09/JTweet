from django.shortcuts import render
from .models import Tweet
from django.views.generic import ListView,DetailView



class TweetDetailView(DetailView):
   template_name = "detail_view.html"
   queryset = Tweet.objects.all()




class TweetListView(ListView):
   template_name = "list_view.html"
   queryset = Tweet.objects.all()
   def get_context_data(self, *args, **kwargs):
       context = super(TweetListView,self).get_context_data(*args, **kwargs)
       return context






