from rest_framework import serializers

from applications.product.models import Category, Product, Image, Rating, Comment


class CategorySerializer(serializers.ModelSerializer):

    def to_representation(self, instance):# для вывода необходимой информации
        representation = super().to_representation(instance)
        print(representation)
        if not instance.parent:
            representation.pop('parent')
        return representation

    class Meta:
        model = Category
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = '__all__'


class CommentCreateSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')# только для чтения не указывать

    class Meta:
        model = Comment
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['likes'] = instance.likes.filter(like=True).count()
        representation['comments'] = CommentSerializer(instance.comment.all(), many=True).data

        rating_res = 0
        for rating in instance.ratings.all():
            rating_res = int(rating.rating)
        try:
            representation['ratings'] = rating_res / instance.ratings.all().count()
        except ZeroDivisionError:
            pass
        return representation
        # return representation
    # TODO: Отобразить рейтинг

    def create(self, validated_data):
        requests = self.context.get('request')
        images = requests.FILES
        product = Product.objects.create(**validated_data)

        for image in images.getlist('images'):
            Image.objects.create(product=product, image=image)

        return product


class RatingSerializer(serializers.Serializer):
    rating = serializers.IntegerField(required=True, min_value=1, max_value=5)


