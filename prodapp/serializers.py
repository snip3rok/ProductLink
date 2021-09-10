from rest_framework import serializers

from .models import ProductLink, Country, Category, Brand, Source


class ProductLinkSerializer(serializers.ModelSerializer):
    country = serializers.SlugRelatedField(slug_field='name', queryset=Country.objects.all())
    category = serializers.SlugRelatedField(slug_field='name', queryset=Category.objects.all())
    brand = serializers.SlugRelatedField(slug_field='name', queryset=Brand.objects.all())
    source = serializers.SlugRelatedField(slug_field='name', queryset=Source.objects.all())

    class Meta:
        model = ProductLink
        fields = ['country', 'category', 'brand', 'link', 'source']
