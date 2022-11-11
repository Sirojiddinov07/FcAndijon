from .models import *
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
import datetime


@login_required(login_url='sign_in')
def Trendings(request):
    user = request.user
    if user.status == 2:
        return render(request, "asd", {"treding": Trending.objects.filter(date__week=datetime.datetime.now().weekday())})
    return redirect("dashboard")


@login_required(login_url='sign_in')
def Create_Trending(request):
    user = request.user
    if user.status == 2:
        if request.method == 'POST':
            video = request.POST['video']
            name = request.POST['name']
            photo = request.POST['photo']
            description = request.POST['description']
            Trending.objects.create(video=video, name=name, photo=photo, description=description)
            return redirect('trendings')
        return redirect('dashboard')
    return redirect('dashboard')


@login_required(login_url='sign_in')
def Update_Trending(request, pk):
    user = request.user
    if user.status == 2:
        if request.method == 'POST':
            video = request.POST['video']
            name = request.POST['name']
            photo = request.POST['photo']
            description = request.POST['description']
            trend = Trending.objects.get(id=pk)
            trend.video = video
            trend.name = name
            trend.photo = photo
            trend.description = description
            trend.save()
            return redirect('trendings')
        return redirect('dashboard')
    return redirect('dashboard')


@login_required(login_url='sign_in')
def Delete_Trending(request, pk):
    user = request.user
    if user.status == 2:
        Trending.objects.get(id=pk).delete()
        return redirect("trendings")
    return redirect('dashboard')


@login_required(login_url='sign_in')
def Sponsors(request):
    user = request.user
    if user.status == 2:
        return render(request, "asdf", {"sponsors": Sponsor.objects.all()})
    return redirect("dashboard")


@login_required(login_url='sign_in')
def Create_Sponsor(request):
    user = request.user
    if user.status == 2:
        if request.method == 'POST':
            photo = request.POST['photo']
            name = request.POST['name']
            Sponsor.objects.create(photo=photo, name=name)
            return redirect('sponsors')
        return redirect('dashboard')
    return redirect('dashboard')


@login_required(login_url='sign_in')
def Update_Sponsor(request, pk):
    user = request.user
    if user.status == 2:
        if request.method == 'POST':
            photo = request.POST['photo']
            name = request.POST['name']
            sponsor = Sponsor.objects.get(id=pk)
            sponsor.photo = photo
            sponsor.name = name
            sponsor.save()
            return redirect('sponsors')
        return redirect('dashboard')
    return redirect('dashboard')


@login_required(login_url='sign_in')
def Delete_Sponsor(request, pk):
    user = request.user
    if user.status == 2:
        Sponsor.objects.get(id=pk).delete()
        return redirect('sponsors')
    return redirect('dashboard')


@login_required(login_url='sign_in')
def SocilMedias(request):
    user = request.user
    if user.status == 2:
        if SocialMedia.objects.last().status == 1:
            return render(request, "asdfa", {"socil": SocialMedia.objects.last()})
        return render(request, "asdfa", {"socil": None})
    return redirect('dashboard')


@login_required(login_url='sign_in')
def Create_SocilMedias(request):
    user = request.user
    if user.status == 2:
        if request.method == "POST":
            inst = request.POST['inst']
            yt = request.POST['yt']
            tt = request.POSt['tt']
            tw = request.POSt['tw']
            fb = request.POST['fb']
            SocialMedia.objects.create(inst=inst, yt=yt, tt=tt, fb=fb, tw=tw)
            return redirect('socilmedias')
        return redirect('dashboard')
    return redirect('dashboard')


@login_required(login_url='sign_in')
def Update_SocilMedias(request, pk):
    user = request.user
    if user.status == 2:
        if request.method == "POST":
            inst = request.POST['inst']
            yt = request.POST['yt']
            tt = request.POSt['tt']
            tw = request.POSt['tw']
            fb = request.POST['fb']
            socil = SocialMedia.objects.get(id=pk)
            socil.inst = inst
            socil.yt = yt
            socil.tt = tt
            socil.tw = tw
            socil.fb = fb
            socil.save()
            return redirect('socilmedias')
        return redirect('dashboard')
    return redirect('dashboard')


@login_required(login_url='sign_in')
def Delete_SocilMedias(request, pk):
    user = request.user
    if user.status == 2:
        socil = SocialMedia.objects.get(id=pk)
        socil.status = 2
        socil.save()
        return redirect('socilmedias')
    return redirect('dashboard')


@login_required(login_url='sign_in')
def Abouts(request):
    user = request.user
    if user.status == 2:
        if About.objects.last().status == 1:
            return render(request, "asdfa", {"socil": About.objects.last()})
        return render(request, "asdfa", {"socil": None})
    return redirect('dashboard')


@login_required(login_url='sign_in')
def Create_Abouts(request):
    user = request.user
    if user.status == 2:
        if request.method == "POST":
            name = request.POST['name']
            photo = request.POST['photo']
            bio = request.POSt['bio']
            SocialMedia.objects.create(name=name, photo=photo, bio=bio)
            return redirect('abouts')
        return redirect('dashboard')
    return redirect('dashboard')


@login_required(login_url='sign_in')
def Update_Abouts(request, pk):
    user = request.user
    if user.status == 2:
        if request.method == "POST":
            name = request.POST['name']
            photo = request.POST['photo']
            bio = request.POSt['bio']
            about = About.objects.get(id=pk)
            about.inst = name
            about.yt = photo
            about.tt = bio
            about.save()
            return redirect('abouts')
        return redirect('dashboard')
    return redirect('dashboard')


@login_required(login_url='sign_in')
def Delete_Abouts(request, pk):
    user = request.user
    if user.status == 2:
        about = About.objects.get(id=pk)
        about.satus = 2
        about.save()
        return redirect('abouts')
    return redirect('dashboard')


def hendler(request, *args, **argv):
    return render(request, "errors-404.html")


@login_required(login_url='sign_in')
def Dashboard(request):
    user = request.user
    if user.status == 1:
        return render(request, "index.html")
    return redirect('sign_in')


@login_required(login_url='sign_in')
def Products(request):
    user = request.user
    if user.status == 1:
        return render(request, "products.html", {"product": Product.objects.filter(status=1)})
    return redirect('dashboard')


@login_required(login_url='sign_in')
def Create_Products(request):
    user = request.user
    if user.status == 1:
        if request.method == "POST":
            name = request.POST['name']
            photo = request.POST['photo']
            price = request.POST['price']
            description = request.POST['description']
            Product.objects.create(name=name, photo=photo, price=price, description=description)
            return redirect('products')
        return redirect('dashboard')
    return redirect('dashboard')


@login_required(login_url='sign_in')
def Update_Products(request, pk):
    user = request.user
    if user.status == 1:
        if request.method == "POST":
            name = request.POST['name']
            photo = request.POST['photo']
            price = request.POST['price']
            description = request.POST['description']
            product = Product.objects.get(id=pk)
            product.name = name
            product.photo = photo
            product.price = price
            product.description = description
            product.save()
            return redirect('products')
        return redirect('dashboard')
    return redirect('dashboard')


@login_required(login_url='sign_in')
def Delete_Products(request, pk):
    user = request.user
    if user.status == 1:
        product = Product.objects.get(id=pk)
        product.status = 2
        product.save()
        return redirect('products')
    return redirect('dashboard')


def Sing_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        users = User.objects.filter(username=username)
        if users is not None:
            usr = authenticate(username=username, password=password)
            if usr is not None:
                if usr.status == 1:
                    login(request, usr)
                    return redirect('dashboard')
                return redirect('hendler')
            return redirect('sign_in')
        return redirect('sign_in')
    return render(request, "auth-login.html")


@login_required(login_url='sign_in')
def Logout(request):
    logout(request)
    return redirect('sign_in')