from django.contrib.auth.models import User
from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView


class IndexView(View):
    @classmethod
    def get_all_users(cls):
        return User.objects.all()

    def get(self, request):
        users = self.get_all_users()
        return render(request, 'index.html', context={'users': users})


class UserListView(ListView):
    model = User
    template_name = 'user_list.html'

    def head(self, *args, **kwargs):
        last_user: User = self.get_queryset().latest('date_joined')
        response = HttpResponse(headers={'Last-Modified': last_user.date_joined.strftime('%a, %d %b %Y %H:^M:%S GMT')})
        return response


class CacheView(IndexView):
    def get(self, request):
        users = cache.get('users')
        if users is None:
            users = self.get_all_users()
            cache.set('users', users, 30)
        users = cache.get('users')
        return HttpResponse(', '.join([user.username for user in users]))

