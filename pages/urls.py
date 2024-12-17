from django.urls import path

from pages.views import (
    home_page_view,
    HomePageView,
    AboutPageView,
)


urlpatterns = [
    path("", home_page_view, name="home"),
    path("hello_view/", HomePageView.as_view(), name="hello_view"),
    path("about/", AboutPageView.as_view(), name="about_view"),
]
