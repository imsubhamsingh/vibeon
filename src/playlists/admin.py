from django.contrib import admin
from playlists.models import Playlist, PlaylistItem

# Register your models here.


class PlaylistItemInline(admin.TabularInline):
    model = PlaylistItem


class PlaylistAdmin(admin.ModelAdmin):
    inlines = [PlaylistItemInline]

    class Meta:
        model = Playlist


admin.site.register(Playlist, PlaylistAdmin)
admin.site.register(PlaylistItem)
