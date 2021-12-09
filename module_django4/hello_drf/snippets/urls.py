from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from snippets import views


# snippet_list = views.SnippetViewSet.as_view({
#     'get': 'list',
#     'post': 'create',
# })
#
# snippet_detail = views.SnippetViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy',
# })
#
# snippet_highlight = views.SnippetViewSet.as_view({
#     'get': 'highlight',
# })
#
# user_list = views.UserViewSet.as_view({
#     'get': 'list',
# })
#
# user_detail = views.UserViewSet.as_view({
#     'get': 'retrieve',
# })

router = DefaultRouter()
router.register('snippets', views.SnippetViewSet)
router.register('users', views.UserViewSet)

urlpatterns = [
    path('',  include(router.urls)),
    # path('', views.api_root),
    # path('snippets/', snippet_list, name='snippet-list'),
    # path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
    # path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
    # path('users/', user_list, name='user-list'),
    # path('users/<int:pk>/', user_detail, name='user-detail'),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
