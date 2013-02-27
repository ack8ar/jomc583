from django.contrib import admin
from roster.models  import Player

class PlayerAdmin(admin.ModelAdmin):
    search_fields = ('name','number',)

admin.site.register(Player,PlayerAdmin)