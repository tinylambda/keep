from django.http import JsonResponse, HttpRequest
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views import View


class IndexView(View):
    def get(self, request):
        return JsonResponse({"view": "IndexView"})


class DetailView(View):
    def get(self, request: HttpRequest, pk):
        # visit http://127.0.0.1:8000/publisher-polls/100/
        # visit http://127.0.0.1:8000/author-polls/100/
        reverse_url = reverse(
            "polls:index", current_app=request.resolver_match.namespace
        )
        return JsonResponse(
            {
                "view": "IndexView",
                "reverse_url": reverse_url,
                "pk": pk,
            }
        )
