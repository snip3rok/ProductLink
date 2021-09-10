from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

from .models import ProductLink
from .serializers import ProductLinkSerializer
from .utils import ProductLinkFilter


class ProductLinkView(generics.ListCreateAPIView):
    serializer_class = ProductLinkSerializer
    queryset = ProductLink.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductLinkFilter
