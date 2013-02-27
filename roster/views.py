# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from roster.models import Player
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    context = {'player_count': Player.objects.count(),
                }
    return render(request,"roster/home.html", context)

def player(request,pk):
    player = get_object_or_404(Player,id=pl)
    return render(request,"roster/player.html", {'player':player})

