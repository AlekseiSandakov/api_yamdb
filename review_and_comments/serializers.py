from rest_framework import serializers

from .models import Comment, Review


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    title = serializers.SlugRelatedField(
        many=False, read_only=True, slug_field="description"
    )

    def validate(self, data):
        author = self.context['request'].user
        title = self.context['view'].kwargs.get('title_id')
        if (self.context.get('request').method == 'POST'
           and Review.objects.filter(title=title, author=author).exists()):
            raise serializers.ValidationError(f'Можно написть только один отзыв')
        return data

    class Meta:
        model = Review
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        many=False,
        slug_field='username',
        read_only=True
    )

    review = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='text'
    )

    class Meta:
        model = Comment
        fields = '__all__'
