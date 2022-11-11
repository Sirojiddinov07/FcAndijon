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
    queryset = Player.objects.all()
    permission_classes = [AllowAny]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = '__all__'


class ClubView(ListAPIView):
    serializer_class = ClubSerializer
    queryset = Club.objects.all()
    permission_classes = [AllowAny]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['name', 'players']


class TurnirView(ListAPIView):
    serializer_class = TurnirSerializer
    queryset = Turnir.objects.all()
    permission_classes = [AllowAny]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = '__all__'


class MatchView(ListAPIView):
    serializer_class = MatchSerializer
    queryset = Match.objects.all()
    permission_classes = [AllowAny]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = '__all__'


class SponsorView(ListAPIView):
    serializer_class = SponsorSerializer
    queryset = Sponsor.objects.all()
    permission_classes = [AllowAny]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = '__all__'


class TrendingView(ListAPIView):
    serializer_class = TrendingSerializer
    queryset = Trending.objects.all()
    permission_classes = [AllowAny]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['description', 'name', 'date']


class WishlistView(ListAPIView):
    serializer_class = WishlistSerializer
    queryset = Wishlist.objects.all()
    permission_classes = [AllowAny]


class CardView(ListAPIView):
    serializer_class = CardSerializer
    queryset = Card.objects.all()
    permission_classes = [IsAuthenticated]


class ProductView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [AllowAny]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['description', 'name', 'price']
    search_fields = ['question_text']
    filter_backends = (filters.SearchFilter,)

class AboutView(ListAPIView):
    serializer_class = AboutSerializer
    queryset = About.objects.all()
    permission_classes = [AllowAny]



