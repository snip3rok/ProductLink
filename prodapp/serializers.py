from rest_framework import serializers

from .models import ProductLink


class ProductLinkSerializer(serializers.ModelSerializer):
    country = serializers.SlugRelatedField(slug_field='name', read_only=True)
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    brand = serializers.SlugRelatedField(slug_field='name', read_only=True)
    source = serializers.SlugRelatedField(slug_field='name', read_only=True)


    class Meta:
        model = ProductLink
        fields = ['country', 'category', 'brand', 'link', 'source']

