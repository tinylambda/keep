import json
import time

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

print("views.py", time.time())


@method_decorator(csrf_exempt, name="dispatch")
class HomeView(View):
    def get(self, request):
        return JsonResponse({"code": 1})

    def post(self, request):
        body_bytes = request.body
        print("body_bytes", body_bytes)
        body_dict = json.loads(body_bytes)
        print("body_dict", body_dict)

        password = body_dict["password"]
        print("password", password)
        from urllib.parse import unquote, unquote_plus

        print(unquote(password))
        print(unquote_plus(password))
        print(password == "7En~8Mk!6Ze$0Yb")
        return JsonResponse({"code": 0})
