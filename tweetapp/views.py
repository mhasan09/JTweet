from django.shortcuts import render
from .models import Tweet
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import TweetModelForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy




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

class TweetUpdateView(UpdateView,LoginRequiredMixin):
    form_class = TweetModelForm
    template_name = 'update_view.html'
    success_url = '/tweet/'
    queryset = Tweet.objects.all()


    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user != self.request.user:
            return 404
        return super(TweetUpdateView, self).dispatch(request, *args, **kwargs)

class TweetDeleteView(DeleteView,LoginRequiredMixin):
    model = Tweet
    success_url = '/tweet/'
    template_name = 'delete_confirm.html'






class TweetListView(ListView):
   template_name = "list_view.html"
   queryset = Tweet.objects.all()
   def get_context_data(self, *args, **kwargs):
       context = super(TweetListView,self).get_context_data(*args, **kwargs)
       return context






