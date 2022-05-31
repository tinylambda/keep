from django.urls import path, register_converter, re_path, include

from . import views

urlpatterns = [
    path("", views.BlogIndexView.as_view()),
    path("archive/", views.BlogArchiveView.as_view()),
]
