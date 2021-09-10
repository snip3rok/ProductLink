from django.urls import path

from .views import ProductLinkView

urlpatterns = [
    path('links', ProductLinkView.as_view()),
]