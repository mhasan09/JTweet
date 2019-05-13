from django.urls import path
from . import views
app_name='tweetapp'
urlpatterns = [

    path('', views.TweetDetailView.as_view(),name="list"),
    path('1/', views.TweetListView.as_view(),name="detail"),



]
