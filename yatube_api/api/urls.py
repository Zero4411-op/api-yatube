from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from .views import PostViewSet, GroupViewSet, CommentViewSet

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('groups', GroupViewSet, basename='groups')

comments_list = CommentViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

comments_detail = CommentViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token, name='api_token_auth'),
    path('v1/posts/<int:post_id>/comments/', comments_list, name='comments'),
    path('v1/posts/<int:post_id>/comments/<int:pk>/',
         comments_detail, name='comment_detail'),
]
