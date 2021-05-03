from django.contrib import admin
from playlists.models import (
    Playlist,
    PlaylistItem,
    TVShowProxy,
    TVShowSeasonProxy,
    MovieProxy,
    PlaylistRelated,
)
from tags.admin import TaggedItemAdmin, TaggedItemInline

# Register your models here.


class MovieProxyAdmin(admin.ModelAdmin):
    list_display = ["title"]
    fields = ["title", "description", "state", "category", "video", "slug"]

    class Meta:
        model = MovieProxy

    def get_queryset(self, request):
        return MovieProxy.objects.all()


admin.site.register(MovieProxy, MovieProxyAdmin)


class SeasonEpisodeInline(admin.TabularInline):
    model = PlaylistItem
    extra = 0


class TVShowSeasonProxyAdmin(admin.ModelAdmin):
    inlines = [SeasonEpisodeInline]
    list_display = ["title", "parent"]

    class Meta:
        model = TVShowSeasonProxy

    def get_queryset(self, request):
        return TVShowSeasonProxy.objects.all()


admin.site.register(TVShowSeasonProxy, TVShowSeasonProxyAdmin)


class TVShowSeasonProxyInline(admin.TabularInline):
    model = TVShowSeasonProxy
    extra = 0
    fields = ["order", "title", "state"]


class TVShowProxyAdmin(admin.ModelAdmin):
    inlines = [TaggedItemInline, TVShowSeasonProxyInline]
    list_display = ["title"]
    fields = ["title", "description", "video", "state", "category", "slug"]

    class Meta:
        model = TVShowProxy

    # explicitely calling  this method
    def get_queryset(self, request):
        return TVShowProxy.objects.all()


admin.site.register(TVShowProxy, TVShowProxyAdmin)


class PlaylistRelatedInline(admin.TabularInline):
    model = PlaylistRelated
    extra = 0
    fk_name = "playlist"


class PlaylistItemInline(admin.TabularInline):
    model = PlaylistItem
    extra = 0


class PlaylistAdmin(admin.ModelAdmin):
    inlines = [PlaylistRelatedInline, PlaylistItemInline]
    fields = ["title", "description", "slug", "state", "active"]

    class Meta:
        model = Playlist

    def get_queryset(self, request):
        return Playlist.objects.filter(type=Playlist.PlaylistTypeChoices.PLAYLIST)


admin.site.register(Playlist, PlaylistAdmin)
admin.site.register(PlaylistItem)
