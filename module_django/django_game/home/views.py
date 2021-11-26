from django.contrib.auth.models import User
from django.core.cache import cache, caches
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, TemplateView


class UserView(ListView):
    model = User

    def head(self, *args, **kwargs):
        last_user: User = self.get_queryset().latest('date_joined')
        response = HttpResponse(
            headers={'Last-Modified': last_user.date_joined.strftime('%a, %d %b %Y %H:%M:%S GMT')}
        )
        return response


class SimpleView(TemplateView):
    template_name = 'simple.html'


class UseCacheView(View):
    @classmethod
    def get_current_users(cls):
        users = User.objects.all()
        return users

    def get(self, request):
        users = cache.get('users')
        if users is None:
            users = self.get_current_users()
            cache.set('users', users, 100)

        users = cache.get('users')
        return HttpResponse(', '.join([user.username for user in users]))


class UseCacheView2(View):
    DB_CACHE = caches['db_cache']

    @classmethod
    def get_current_users(cls):
        users = User.objects.all()
        return users

    def get(self, request):
        users = self.DB_CACHE.get('users')
        if users is None:
            users = self.get_current_users()
            self.DB_CACHE.set('users', users, 100)

        users = self.DB_CACHE.get('users')
        return HttpResponse(', '.join([user.username for user in users]))

