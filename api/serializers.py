from rest_framework.serializers import ModelSerializer
from adminka.models import *

class PlayerSerializer(ModelSerializer):
    class Meta:
        model = Player
        fields = "__all__"


class ClubSerializer(ModelSerializer):
    class Meta:
        model = Club
        fields = "__all__"


class TurnirSerializer(ModelSerializer):
    class Meta:
        model = Turnir
        fields = "__all__"


class MatchSerializer(ModelSerializer):
    class Meta:
        model = Match
        fields = "__all__"


class SponsorSerializer(ModelSerializer):
    class Meta:
        model = Sponsor
        fields = "__all__"


class TrendingSerializer(ModelSerializer):
    class Meta:
        model = Trending
        fields = "__all__"


class CardSerializer(ModelSerializer):
    class Meta:
        model = Card
        fields = "__all__"


class WishlistSerializer(ModelSerializer):
    class Meta:
        model = Wishlist
        fields = "__all__"


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


