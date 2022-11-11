from .viewset import *
from django.urls import path

urlpatterns = [
    path('products/', Products, name="products"),
    path('create_products/', Create_Products, name="create_products"),
    path('update_products/<int:pk>/', Update_Products, name="update_products"),
    path('delete_products/<int:pk>/', Delete_Products, name="delete_products"),
    path('', Dashboard, name="dashboard"),
    path('trendings/', Trendings, name="trendings"),
    path('sponsors/', Sponsors, name="sponsors"),
    path('socilmedias/', SocilMedias, name="socilmedias"),
    path('abouts/', Abouts, name="abouts"),
    path('create_trending/', Create_Trending, name="create_trending"),
    path('create_sponsor/', Create_Sponsor, name="create_sponsor"),
    path('create_socilmedia/', Create_SocilMedias, name="create_socilmedia"),
    path('create_about/', Create_Abouts, name="create_about"),
    path('update_trending/<int:pk>/', Update_Trending, name="update_trending"),
    path('update_sponsor/<int:pk>/', Update_Sponsor, name="update_sponsor"),
    path('update_socilmedia/<int:pk>/', Update_SocilMedias, name="update_socilmedia"),
    path('update_about/<int:pk>/', Update_Abouts, name="update_about"),
    path('delete_trending/<int:pk>/', Delete_Trending, name="delete_trending"),
    path('delete_sponsor/<int:pk>/', Delete_Sponsor, name="delete_sponsor"),
    path('delete_socilmedia/<int:pk>/', Delete_SocilMedias, name="delete_socilmedia"),
    path('delete_about/<int:pk>/', Delete_Abouts, name="delete_about"),
    path("sign_in/", Sing_in, name="sign_in"),
    path("logout/", Logout, name="logout"),
]