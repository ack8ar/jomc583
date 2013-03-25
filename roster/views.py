# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from roster.models import Player, Team, News
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    context = {'player_count': Player.objects.count(),
                }
    return render(request,"roster/home.html", context)

def team(request,pk):
    team = get_object_or_404(Team,id=pk)
    player = Player.objects.values().filter(team=1)
    news = News.objects.values()
    context = {
            'team': team, 'news':news, 'player':player
            }
    return render(request,"roster/team.html", context)

def player(request,pk):
    player = get_object_or_404(Player,id=pk)
    f = str(player.height/12)
    i = str(player.height%12)
    player.height = "%s'%s" %(f,i)
    return render(request,"roster/player.html", {'player':player,'team':team, 'number':player, 'image_url':player,
                                                 'position':player,'year':player,'hometown':player,'state':player,
                                                 'high_school':player,'bio':player, 'height':player.height})


