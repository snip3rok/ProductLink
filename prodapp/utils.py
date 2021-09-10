from django_filters import rest_framework as filters
from django.http import HttpResponse
import csv

from .models import ProductLink, Country


def export_to_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="ProductLink.csv"'
    writer = csv.writer(response)
    writer.writerow(['source', 'country', 'brand', 'category', 'link'])
    product_links = queryset.values_list('source__name', 'country__name', 'brand__name', 'category__name', 'link')
    for link in product_links:
        writer.writerow(link)
    return response


export_to_csv.short_description = 'Export to csv'


class ProductLinkFilter(filters.FilterSet):
    country = filters.BaseInFilter(field_name='country__name')
    source = filters.BaseInFilter(field_name='source__name')

    class Meta:
        model = ProductLink
        fields = ('country', 'source')