from django.contrib import admin
from videos.models import VideoAllProxy, VideoPublishedProxy

# Register your models here.


class VideoAllAdmin(admin.ModelAdmin):
    list_display = ["title", "video_id", "is_published", "state"]
    search_fields = ["title"]
    list_filter = ["active", "state"]
    readonly_fields = ["id", "is_published", "publish_timestamp"]

    class Meta:
        model = VideoAllProxy

    # def published(self, obj, *args, **kwargs):
    #     return obj.active


class VideoPublishedProxyAdmin(admin.ModelAdmin):
    list_display = ["title", "video_id"]
    search_fields = ["title"]

    class Meta:
        model = VideoPublishedProxy

    def get_queryset(self, request):
        return VideoAllProxy.objects.filter(active=True)


admin.site.register(VideoAllProxy, VideoAllAdmin)
admin.site.register(VideoPublishedProxy, VideoPublishedProxyAdmin)
