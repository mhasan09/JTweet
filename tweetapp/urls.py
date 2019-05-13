from django.urls import path
from . import views
app_name='tweetapp'
urlpatterns = [
    path('', views.TweetListView.as_view(),name="detail"),
    path('<int:pk>/', views.TweetDetailView.as_view(),name="list"),




]
