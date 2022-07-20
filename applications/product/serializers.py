from rest_framework import serializers

from applications.product.models import Category, Product, Image


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


class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        requests = self.context.get('request')
        images = requests.FILES
        product = Product.objects.create(**validated_data)

        for image in images.getlist('images'):
            Image.objects.create(product=product, image=image)

        return product

