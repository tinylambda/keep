from django.urls import path, register_converter, re_path, include

from . import views, converters

register_converter(converters.FourDigitYearConverter, "yyyy")

urlpatterns = [
    path("official-site/<path:p>/", views.UrlTestPathView.as_view(), name="get path"),
    path(
        "timecategory/<yyyy:year>/",
        views.UrlTestCustomConverterView.as_view(),
        name="custom converter",
    ),
    re_path(
        r"^timecategory/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$",
        views.UrlTestRePathView.as_view(),
        name="re_path test",
    ),
    re_path(
        r"^comments/(?:page-(?P<page_number>\d+))$", views.UrlNestedArguments.as_view()
    ),
    path(
        "mybooks/",
        views.UrlDefaultViewParameterValueView.as_view(),
        name="book-page-no-num",
    ),
    path(
        "mybooks/page<int:num>/",
        views.UrlDefaultViewParameterValueView.as_view(),
        name="book-page",
    ),
    path(
        "<page_slug>-<page_id>/",
        include(
            [
                path("history/", views.UrlIncludeViewOne.as_view()),
                path("edit/", views.UrlIncludeViewTwo.as_view()),
            ]
        ),
    ),
    path("urlreverse/", views.UrlReverseTest.as_view()),
]
