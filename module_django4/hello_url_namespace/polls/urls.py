from django.urls import path, register_converter, re_path

from . import views, converters

register_converter(converters.FourDigitYearConverter, 'yyyy')

urlpatterns = [
    path('', views.IndexView.as_view(), name='polls.index'),
    path('mypath/<path:p>/', views.UrlTestPathView.as_view(), name='url test path view'),
    path('books/<yyyy:year>/', views.UrlTestCustomConverterView.as_view(), name='custom converter'),
    re_path(r'^books/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.UrlTestRePathView.as_view(), name='re_path test'),
]

