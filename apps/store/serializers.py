from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer, CharField

from apps.store.models import Product, Category


class ProductSerializer(ModelSerializer):
    # full_name = CharField(source='get_full_name')
    category = SlugRelatedField(slug_field='title', read_only=True)
    class Meta:
        model = Product
        # fields = '__all__'
        fields = ['title', 'slug', 'description', 'price', 'category']


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category

        fields = ['title', 'slug']


