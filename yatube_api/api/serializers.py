from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.generics import get_object_or_404

from posts.models import Comment, Follow, Group, Post


User = get_user_model()


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
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')
        read_only_fields = ('id', 'author', 'post')


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(read_only=True,
                                        slug_field='username')
    following = serializers.SlugRelatedField(queryset=User.objects.all(),
                                             slug_field='username',)

    def validate(self, data):
        user = get_object_or_404(User, username=data['following'].username)
        follow = Follow.objects.filter(user=self.context['request'].user, following=user).exists()
        if user == self.context['request'].user:
            raise serializers.ValidationError("Нельзя подписаться саму на себя")
        if follow is True:
            raise serializers.ValidationError("Вы уже подписаны на пользователя")
        return data

    class Meta:
        model = Follow
        fields = ('user', 'following')
        read_only_fields = ('id', 'user')