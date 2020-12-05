from rest_framework.serializers import ModelSerializer

from apps.blog.models.blog import Post, PostComment, MinorPostComment


class MinorPostCommentSerializer(ModelSerializer):
    class Meta:
        model = MinorPostComment
        fields = ('id', 'comment', 'author', 'text', 'created', 'last_modified')
        extra_kwargs = {
            'author': {'read_only': True},
            'created': {'read_only': True},
            'last_modified': {'read_only': True},
        }


class PostCommentSerializer(ModelSerializer):
    minor_comment = MinorPostCommentSerializer(many=True, read_only=True)

    class Meta:
        model = PostComment
        fields = ('id', 'post', 'author', 'text', 'minor_comment', 'created', 'last_modified')
        extra_kwargs = {
            'author': {'read_only': True},
            'minor_comment': {'read_only': True},
            'created': {'read_only': True},
            'last_modified': {'read_only': True},
        }


class PostSerializer(ModelSerializer):
    post_comment = PostCommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('author', 'title', 'tags', 'text', 'created', 'last_modified')
