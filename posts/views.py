from django.views.generic import ListView, DetailView
from posts.models import Post


class HomePageView(ListView):
    model = Post
    template_name = "home.html"


class PostView(DetailView):
    model = Post
    template_name = "post.html"
