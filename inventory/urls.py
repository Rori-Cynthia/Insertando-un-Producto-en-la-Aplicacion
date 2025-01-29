from django.urls import path

from .views import (
    HomeView,
    ProductListView,
    ProductInputView,
)

urlpatterns = [
    path("", HomeView.as_view(), name='index'),
    path("add/", ProductInputView.as_view(), name='add_product'),
    path("information/", ProductListView.as_view(), name='info_product'),
]
