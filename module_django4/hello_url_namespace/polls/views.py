from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import ListView


class IndexView(View):
    def get(self, request):
        result = reverse(
            "polls:index", current_app=self.request.resolver_match.namespace
        )
        return render(request, "poll-author.html")
