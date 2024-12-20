from django.urls import path

from posts.views import HomePageView, PostView


urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("post/<int:pk>/", PostView.as_view(), name="post_detail"),
]
