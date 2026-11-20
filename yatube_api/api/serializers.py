from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

from posts.models import Comment, Group, Follow, Post, User


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field="username", read_only=True
    )

    class Meta:
        fields = "__all__"
        model = Post


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели подписок на авторов.."""

    following = serializers.SlugRelatedField(
        slug_field="username", queryset=User.objects.all()
    )
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field="username",
        default=CurrentUserDefault(),
    )

    def validate_following(self, following):
        if self.context["request"].user == following:
            raise serializers.ValidationError(
                "You can't subscribe to yourself"
            )
        return following

    class Meta:
        fields = "__all__"
        model = Follow
        validators = (
            serializers.UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=("user", "following"),
                message="You have already subscribed to this author",
            ),
        )


class CommentSerializer(serializers.ModelSerializer):
    """Сериалайзер для комментариев."""

    author = serializers.SlugRelatedField(
        read_only=True, slug_field="username"
    )

    class Meta:
        fields = "__all__"
        read_only_fields = ("post", "author")
        model = Comment
