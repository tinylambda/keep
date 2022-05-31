from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView
import django.contrib.admin


class UrlTestPathView(View):
    def get(self, request, p):
        # visit http://127.0.0.1:8000/books/official-site/this/is/a/good/path/ to test
        return JsonResponse({"p": p})


class UrlTestCustomConverterView(View):
    def get(self, request, year):
        # visit http://127.0.0.1:8000/books/timecategory/2024/ to test
        return JsonResponse({"year": year, "year_type": str(type(year))})


class UrlTestRePathView(View):
    def get(self, request, year, month):
        # visit http://127.0.0.1:8000/books/timecategory/2024/12/ to test
        return JsonResponse(
            {"year": year, "month": month, "year_type": str(type(year))}
        )


class UrlNestedArguments(View):
    def get(self, request, page_number):
        # visit http://127.0.0.1:8000/books/comments/page-222 to test
        return JsonResponse(
            {"page_number": page_number, "page_number_type": str(type(page_number))}
        )


class UrlDefaultViewParameterValueView(View):
    def get(self, request, num=1):
        # visit http://127.0.0.1:8000/books/mybooks/page100/
        # visit http://127.0.0.1:8000/books/mybooks/
        return JsonResponse({"num": num, "num_type": str(type(num))})


class UrlIncludeViewOne(View):
    def get(self, request, page_slug, page_id):
        # visit http://127.0.0.1:8000/books/test-123/history/
        return JsonResponse(
            {"view": "UrlIncludeViewOne", "page_slug": page_slug, "page_id": page_id}
        )


class UrlIncludeViewTwo(View):
    def get(self, request, page_slug, page_id):
        # visit http://127.0.0.1:8000/books/test-123/edit/
        return JsonResponse(
            {"view": "UrlIncludeViewTwo", "page_slug": page_slug, "page_id": page_id}
        )


class UrlReverseTest(TemplateView):
    # visit http://127.0.0.1:8000/books/urlreverse/ to test
    template_name = "urlreverse.html"

    def get(self, request, *args, **kwargs):
        for i in range(10):
            print(reverse("book-page", args=(i,)))
        return super().get(request, *args, **kwargs)
