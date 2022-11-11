from django.shortcuts import render
from .models import *





# def addplayer(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         date_birth = request.POST['date_birth']
#         description = request.POST['description']
#         last_name = request.POST['last_name']
#         played_minutes = request.POST['played_minutes']
#         sub_off = request.POST['sub_off']
#         games = request.POST['games']
#         number = request.POST['number']
#         status = request.POST['status']
#         captain = request.POST['captain']
#         Player.objects.create(name=name,date_birth=date_birth,description=description,last_name=last_name,played_minutes=played_minutes,sub_off=sub_off,games=games,number=number,status=status,captain=captain)
#         return render(request\)