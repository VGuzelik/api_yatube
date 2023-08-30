from posts.models import Comment, Follow, Group, Post, User
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment
        read_only_fields = ('post',)


class FollowSerializer(serializers.ModelSerializer):
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects
    )
    user = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects,
        default=serializers.CurrentUserDefault(),
    )

    class Meta:
        fields = '__all__'
        model = Follow
        validators = (
            UniqueTogetherValidator(
                queryset=Follow.objects,
                fields=('user', 'following'),
            ),
        )

    def validate(self, data):
        if data['user'] != data['following']:
            return data
        raise serializers.ValidationError(
            'Нельзя подписаться на самого себя'
        )


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Group
