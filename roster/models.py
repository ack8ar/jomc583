from django.db import models

# Create your models here.

class Team(models.Model):
    team = models.CharField(unique=False, max_length=50)
    wins = models.IntegerField(unique=False,max_length=3)
    losses = models.IntegerField(unique=False,max_length=3)
    accWins = models.IntegerField(unique=False,max_length=3)
    accLoss = models.IntegerField(unique=False,max_length=3)
    
    def __unicode__(self):
        return U'%s' %(self.team)

class News(models.Model):
    headline = models.CharField(max_length=100)
    article = models.CharField(max_length=2000)
    author = models.CharField(max_length=100)
    org = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    team = models.ForeignKey(Team)
    
    def __unicode__(self):
        return U'%s %s %s' %(self.pk, self.team,self.headline)

class Player(models.Model):
    team = models.ForeignKey('Team')
    name = models.CharField(unique=False, max_length=50)
    number = models.IntegerField(unique=True,max_length=2)
    height = models.IntegerField(unique=False, max_length=4)
    weight = models.IntegerField(max_length=3)
    position = models.CharField(max_length=7)
    year = models.CharField(max_length=10)
    hometown = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    high_school = models.CharField(max_length=100)
    image_url = models.CharField(max_length=100)
    bio = models.CharField(max_length=2000)
    class Meta(object):
        ordering = ('number','name')
        
    def __unicode__(self):
        return U'%s %s %s %s' %(self.name,self.number,self.team,self.number)
    
#class Stats(models.Model):
#    player = models.ForeignKey('number.Player')
#    gp = models.IntegerField("games played",max_length=3)
#    gs = models.IntegerField("games started",max_length=3)
#    miPlayed = models.IntegerField("minutes played",max_length=5)
#    fga = models.IntegerField("field goals attempted",max_length=3)
#    fgm = models.IntegerField("field goals made",max_length=3)
#    thrga = models.IntegerField("three pointers attempted",max_length=3)
#    thrgm = models.IntegerField("three pointers made",max_length=3)
#    oreb = models.IntegerField("offensive rebounds",max_length=3)
#    dreb = models.IntegerField("defensive rebounds",max_length=3)
#    pf = models.IntegerField("personal fouls",max_length=3)
#    asst = models.IntegerField("assists",max_length=3)
#    to = models.IntegerField("turnovers",max_length=3)
#    fta = models.IntegerField("free throws attempted",max_length=3)
#    ftm = models.IntegerField("free throws made",max_length=3)
#    stl = models.IntegerField("steals",max_length=3)

    