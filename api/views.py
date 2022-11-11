from django.shortcuts import render
from adminka.models import *
from .serializers import *
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
import django_filters.rest_framework
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination

# Create your views here.
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000



class PlayersView(ListAPIView):
    serializer_class = PlayerSerializer
    queryset = Player()
    permission_classes = [AllowAny]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = '__all__'

class ClubView(ListAPIView):
    serializer_class = ClubSerializer
    queryset = Club()
    permission_classes = [AllowAny]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = '__all__'


class TurnirView(ListAPIView):
    serializer_class = TurnirSerializer
    queryset = Turnir()
    permission_classes = [AllowAny]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = '__all__'


class MatchView(ListAPIView):
    serializer_class = MatchSerializer
    queryset = Match()
    permission_classes = [AllowAny]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = '__all__'


class SponsorView(ListAPIView):
    serializer_class = SponsorSerializer
    queryset = Sponsor()
    permission_classes = [AllowAny]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = '__all__'


class TrendingView(ListAPIView):
    serializer_class = TrendingSerializer
    queryset = Trending()
    permission_classes = [AllowAny]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = '__all__'


class WishlistView(ListAPIView):
    serializer_class = WishlistSerializer
    queryset = Wishlist()
    permission_classes = [AllowAny]


class CardView(ListAPIView):
    serializer_class = CardSerializer
    queryset = Card()
    permission_classes = [IsAuthenticated]



class ProductView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product()
    permission_classes = [AllowAny]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = '__all__'
    pagination_class = StandardResultsSetPagination



