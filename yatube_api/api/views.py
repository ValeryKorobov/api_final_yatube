from django.shortcuts import get_object_or_404
from posts.models import Follow, Group, Post, User
from rest_framework import filters, mixins, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from .permissions import IsAuthorOrReadOnly
from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer)


class PostViewSet(viewsets.ModelViewSet):
    """Вьюсет для обьектов модели Post."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        """Создает запись, где автором является текущий пользователь."""
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для обьектов модели Group."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FollowViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet
                    ):
    """Вьюсет для обьектов модели Follow."""
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ('user__username', 'following__username')

    def get_queryset(self):
        """Возвращает queryset c подписчиками данного пользователя."""
        user = get_object_or_404(User, username=self.request.user)
        return user.follower.all()

    def perform_create(self, serializer):
        """Подписывает пользователя на другого юзера."""
        serializer.save(user=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """Вьюсет для обьектов модели Comment."""
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def get_post(self):
        """Возвращает обект поста."""
        post_id = self.kwargs.get('post_id')
        return get_object_or_404(Post, pk=post_id)

    def get_queryset(self):
        """Возвращает queryset c комментариями для текущей записи."""
        return self.get_post().comments.all()

    def perform_create(self, serializer):
        """Создает комментарий для текущего поста,
        где автором является текущий пользователь."""
        serializer.save(
            author=self.request.user,
            post=self.get_post()
        )
