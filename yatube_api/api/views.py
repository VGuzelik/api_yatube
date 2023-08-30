from django.shortcuts import get_object_or_404
from posts.models import Group, Post, User
from rest_framework import filters, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from .mixins import ListCreateViewSet
from .permissions import CastomPermission
from .serializers import (
    CommentSerializer,
    FollowSerializer,
    GroupSerializer,
    PostSerializer
)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects
    serializer_class = GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.select_related('author', 'group')
    serializer_class = PostSerializer
    permission_classes = (
        CastomPermission,
    )
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (
        CastomPermission,
    )

    def get_post(self):
        post_id = self.kwargs.get('post_id')
        return get_object_or_404(Post, id=post_id)

    def get_queryset(self):
        post = self.get_post()
        new_queryset = post.comments
        return new_queryset

    def perform_create(self, serializer):
        post = self.get_post()
        serializer.save(author=self.request.user, post_id=post.id)


class FollowViewSet(ListCreateViewSet):
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)
    permission_classes = (IsAuthenticated, CastomPermission,)

    def get_queryset(self):
        user = get_object_or_404(User, id=self.request.user.id)
        return user.follower

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
