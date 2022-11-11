from django.urls import path
from .views import *


urlpatterns = [
    path('players/', PlayersView.as_view()),
    path('club/', ClubView.as_view()),
    path('turnir/', TurnirView.as_view()),
    path('match/', MatchView.as_view()),
    path('sponsor/', SponsorView.as_view()),
    path('trending/', TrendingView.as_view()),
    path('wishlist/', WishlistView.as_view()),
    path('card/', CardView.as_view()),
    path('product/', ProductView.as_view()),
]