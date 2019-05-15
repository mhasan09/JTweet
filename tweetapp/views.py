from django.shortcuts import render
from .models import Tweet
from django.views.generic import ListView, DetailView, CreateView
from .forms import TweetModelForm
from django.contrib.auth.mixins import LoginRequiredMixin




class TweetDetailView(DetailView):
   template_name = "detail_view.html"
   queryset = Tweet.objects.all()

class TweetCreateView(CreateView,LoginRequiredMixin):
    login_url = 'admin/'
    form_class = TweetModelForm
    template_name = 'create_view.html'
    success_url = '/tweet/create/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TweetCreateView, self).form_valid(form)




class TweetListView(ListView):
   template_name = "list_view.html"
   queryset = Tweet.objects.all()
   def get_context_data(self, *args, **kwargs):
       context = super(TweetListView,self).get_context_data(*args, **kwargs)
       return context






