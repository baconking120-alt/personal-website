from django.urls import path

from .views import (
    home_page_view,
    AboutPageView,
    ContactPageView,
    ProductsPageView,
)

urlpatterns = [
    path("", home_page_view, name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("contact/", ContactPageView.as_view(), name="contact"),
    path("products/", ProductsPageView.as_view(), name="products"),
]