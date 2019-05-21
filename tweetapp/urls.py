from django.urls import path
from .views import TweetCreateView,TweetListView,TweetDetailView,TweetUpdateView, TweetDeleteView
from django.contrib.auth.decorators import login_required
from django.views.generic.base import RedirectView
app_name='tweetapp'
urlpatterns = [
    path('',RedirectView.as_view(url="/")),
    path('search/', TweetListView.as_view(),name="list"),
    path('<int:pk>/', TweetDetailView.as_view(),name="detail"),
    path('create/', login_required(TweetCreateView.as_view()),name="create"),
    path('<int:pk>/update/', login_required(TweetUpdateView.as_view()),name="update"),
    path('<int:pk>/delete/', login_required(TweetDeleteView.as_view()),name="delete"),




]
