from django.urls import path
from . import views
app_name='tweetapp'
urlpatterns = [

    path('', views.TweetListView.as_view(),name="list"),


]
