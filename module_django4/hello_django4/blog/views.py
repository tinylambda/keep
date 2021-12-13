from django.http import JsonResponse
from django.shortcuts import render
from django.views import View


class BlogIndexView(View):
    def get(self, request, username, foo):
        # visit http://127.0.0.1:8000/felix/blog/
        return JsonResponse({'view': 'BlogView', 'username': username, 'foo': foo})


class BlogArchiveView(View):
    def get(self, request, username, foo):
        # visit http://127.0.0.1:8000/felix/blog/archive/
        return JsonResponse({'view': 'BlogArchiveView', 'username': username, 'foo': foo})
