from django.urls import path
from .views import TweetCreateView,TweetListView,TweetDetailView,TweetUpdateView
from django.contrib.auth.decorators import login_required
app_name='tweetapp'
urlpatterns = [
    path('', TweetListView.as_view(),name="detail"),
    path('<int:pk>/', TweetDetailView.as_view(),name="list"),
    path('create/', login_required(TweetCreateView.as_view()),name="create"),
    path('<int:pk>/update/', login_required(TweetUpdateView.as_view()),name="update"),




]
