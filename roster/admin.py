from django.contrib import admin
from roster.models  import Player, Team, News

class PlayerAdmin(admin.ModelAdmin):
    search_fields = ('name','number',)

admin.site.register(Player,PlayerAdmin)

class TeamAdmin(admin.ModelAdmin):
    search_field = ('team',)    
admin.site.register(Team,TeamAdmin)

class NewsAdmin(admin.ModelAdmin):
    search_field = ('team', 'headline')
admin.site.register(News,NewsAdmin)