from django.shortcuts import render
from .models import Tweet
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import TweetModelForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q




class TweetDetailView(DetailView):
   template_name = "detail_view.html"
   queryset = Tweet.objects.all()

class TweetCreateView(CreateView,LoginRequiredMixin):
    login_url = 'admin/'
    form_class = TweetModelForm
    template_name = 'create_view.html'
    success_url = '/tweet/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TweetCreateView, self).form_valid(form)

class TweetUpdateView(UpdateView,LoginRequiredMixin):
    form_class = TweetModelForm
    template_name = 'update_view.html'
    success_url = reverse_lazy("tweetapp:list")
    queryset = Tweet.objects.all()


    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user != self.request.user:
            return 404
        return super(TweetUpdateView, self).dispatch(request, *args, **kwargs)

class TweetDeleteView(DeleteView,LoginRequiredMixin):
    model = Tweet
    success_url = reverse_lazy("tweetapp:list")
    template_name = 'delete_confirm.html'






class TweetListView(ListView):
   template_name = "list_view.html"
   def get_context_data(self, *args, **kwargs):
       context = super(TweetListView,self).get_context_data(*args, **kwargs)
       return context

   def get_queryset(self,*args,**kwargs):
       qs=Tweet.objects.all()
       query=self.request.GET.get("q",None)
       if query is not None:
           qs=qs.filter(

               Q(content__icontains=query) |
               Q(user__username__icontains=query)

           )

       return qs







