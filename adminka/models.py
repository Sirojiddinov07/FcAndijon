from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    status = models.SmallIntegerField(default=2, choices=((1, "admin"), (2, "user")))


class Player(models.Model):
    name = models.CharField(max_length=23232)
    date_birth = models.DateField()
    description = models.CharField(max_length=10000)
    last_name = models.CharField(max_length=23232)
    played_minutes = models.IntegerField(default=0)
    sub_off = models.IntegerField(default=0)
    games = models.IntegerField(default=0)
    number = models.IntegerField()
    TYPE = (
        (1, 'attacker'),     #нападающий
        (2, 'midfielder'),   #полузащитник
        (3, 'defender'),     #защитник
        (4, 'goalkeeper'),   #вратарь
        (6, 'substitute'),    #замена
    )
    status = models.SmallIntegerField(default=6, choices=TYPE)
    captain = models.BooleanField(default=False)


class Club(models.Model):
    players = models.ManyToManyField(Player)
    name = models.CharField(max_length=2323232)
    photo = models.ImageField(upload_to='Club/')
    scored = models.IntegerField(default=0)
    missed = models.IntegerField(default=0)
    game = models.IntegerField(default=0)
    scores = models.IntegerField(default=0)


class Turnir(models.Model):
    date = models.DateTimeField()
    club = models.ManyToManyField(Club)
    name = models.CharField(max_length=23232)


class Match(models.Model):
    date = models.DateTimeField()
    turnir = models.ForeignKey(Turnir, on_delete=models.CASCADE)
    club1 = models.ForeignKey(Club, related_name='ffffff', on_delete=models.CASCADE)
    club2 = models.ForeignKey(Club, related_name='sdsdsds', on_delete=models.CASCADE)
    club_1_result = models.IntegerField()
    club_2_result = models.IntegerField()


class Trending(models.Model):
    date = models.DateField(auto_now_add=True)
    video = models.FileField(null=True, blank=True)
    name = models.CharField(max_length=2323)
    photo = models.ImageField(upload_to='Trending/')
    description = models.CharField(max_length=65676876)


class Sponsor(models.Model):
    photo = models.ImageField(upload_to='Sponsor/')
    name = models.CharField(max_length=344343)


class Product(models.Model):
    name = models.CharField(max_length=23232)
    photo = models.ImageField(upload_to="Product/")
    price = models.IntegerField()
    description = models.CharField(max_length=23232)
    status = models.SmallIntegerField(default=1, choices=((1, "in work"), (2, "deleted")))


class Wishlist(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Card(models.Model):
    quantity = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class SocialMedia(models.Model):
    inst = models.URLField()
    yt = models.URLField()
    tt = models.URLField()
    tw = models.URLField()
    fb = models.URLField()
    status = models.SmallIntegerField(default=1, choices=((1, "in work"), (2, "deleted")))


class About(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="About/")
    bio = models.TextField()
    status = models.SmallIntegerField(default=1, choices=((1, "in work"), (2, "deleted")))