from django.urls import path, register_converter, re_path

from . import views, converters

register_converter(converters.FourDigitYearConverter, "yyyy")

urlpatterns = [
    path("", views.IndexView.as_view(), name="polls.index"),
]
