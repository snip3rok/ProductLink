from rest_framework import generics, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from .models import ProductLink
from .serializers import ProductLinkSerializer
from .utils import ProductLinkFilter


class ProductLinkView(generics.ListAPIView):
    serializer_class = ProductLinkSerializer
    queryset = ProductLink.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductLinkFilter
