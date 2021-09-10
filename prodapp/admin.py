from django.contrib import admin

from .models import ProductLink, Source, Brand
from .utils import export_to_csv


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(ProductLink)
class ProductLinkAdmin(admin.ModelAdmin):
    list_display = ['id', 'link', 'source', 'country', 'brand', 'category']
    list_display_links = ['id', 'link']
    actions = [export_to_csv, ]
