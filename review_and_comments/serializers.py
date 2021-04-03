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
<<<<<<< HEAD
        if (self.context.get('request').method == 'POST'
           and Review.objects.filter(title=title, author=author).exists()):
            raise serializers.ValidationError(f'Можно написть только один отзыв')
=======
        method = self.context.get('request').method == 'POST'
        if (method
           and Review.objects.filter(title=title, author=author).exists()):
            raise serializers.ValidationError(
                'Можно написть только один отзыв'
            )
>>>>>>> 08549b4e8d21c23ff4223bbb065eaa23cac4e507
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
