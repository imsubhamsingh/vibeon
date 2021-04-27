from django.test import TestCase
from playlists.models import TVShowProxy, TVShowSeasonProxy
from vibeon.db.models import PublishStateOptions
from django.utils import timezone
from django.utils.text import slugify
from videos.models import Video

# Create your tests here.


class TVShowProxyModelTestCase(TestCase):
    def create_shows_with_seasons(self):
        the_office = TVShowProxy.objects.create(title="The Office Series")
        season_1 = TVShowSeasonProxy.objects.create(
            title="The Office Series Season 1",
            state=PublishStateOptions.PUBLISH,
            parent=the_office,
            order=1,
        )
        season_2 = TVShowSeasonProxy.objects.create(
            title="The Office Series Season 2", parent=the_office, order=2
        )
        season_3 = TVShowSeasonProxy.objects.create(
            title="The Office Series Season 3", parent=the_office, order=3
        )
        season_4 = TVShowSeasonProxy.objects.create(
            title="The Office Series Season 4", parent=the_office, order=4
        )
        shows = TVShowProxy.objects.filter(parent__isnull=True)
        self.show = the_office

    def create_videos(self):
        video_a = Video.objects.create(title="My title", video_id="100")
        video_b = Video.objects.create(title="My title", video_id="101")
        video_c = Video.objects.create(title="My title", video_id="102")
        self.video_a = video_a
        self.video_b = video_b
        self.video_c = video_c
        self.video_qs = Video.objects.all()

    def setUp(self):
        self.create_videos()
        self.create_shows_with_seasons()
        self.obj_a = TVShowProxy.objects.create(title="Scam 1992", video=self.video_a)
        obj_b = TVShowProxy.objects.create(
            title="this is my title",
            state=PublishStateOptions.PUBLISH,
            video=self.video_a,
        )
        obj_b.videos.set(self.video_qs)
        obj_b.save()
        self.obj_b = obj_b

    def test_show_has_seasons(self):
        seasons = self.show.playlist_set.all()
        self.assertTrue(seasons.exists())
        self.assertEqual(seasons.count(), 4)

    def test_playlist_video(self):
        self.assertEqual(self.obj_a.video, self.video_a)

    def test_video_playlist(self):
        qs = self.video_a.playlist_featured.all()
        self.assertEqual(qs.count(), 2)

    def test_playlist_through_model(self):
        v_qs = sorted(list(self.video_qs.values_list("id")))
        video_qs = sorted(list(self.obj_b.videos.all().values_list("id")))
        playlist_item_qs = sorted(
            list(self.obj_b.playlistitem_set.all().values_list("video"))
        )
        self.assertEqual(v_qs, video_qs, playlist_item_qs)

    def test_slug_field(self):
        title = self.obj_a.title
        test_slug = slugify(title)
        self.assertEqual(test_slug, self.obj_a.slug)

    def test_valid_title(self):
        title = "Scam 1992"
        qs = TVShowProxy.objects.all().filter(title=title)
        self.assertTrue(qs.exists())

    def test_tv_shows_created_count(self):
        title = "Scam 1992"
        qs = TVShowProxy.objects.all()
        self.assertTrue(qs.count(), 3)

    def test_seasons_created_count(self):
        title = "Scam 1992"
        qs = TVShowProxy.objects.all()
        self.assertTrue(qs.count(), 3)

    def test_tv_show_draft_case(self):
        qs = TVShowProxy.objects.all().filter(state=PublishStateOptions.DRAFT)
        self.assertEqual(qs.count(), 2)

    def test_seasons_draft_case(self):
        qs = TVShowSeasonProxy.objects.all().filter(state=PublishStateOptions.DRAFT)
        self.assertEqual(qs.count(), 3)

    def test_publish_case(self):
        qs = TVShowProxy.objects.all().filter(state=PublishStateOptions.PUBLISH)
        now = timezone.now()
        published_qs = TVShowProxy.objects.all().filter(publish_timestamp__lte=now)
        self.assertTrue(published_qs.exists())

    def test_publish_manager(self):
        published_qs = TVShowProxy.objects.all().published()
        published_qs_2 = TVShowProxy.objects.all().published()
        self.assertTrue(published_qs.exists())
        self.assertEqual(published_qs.count(), published_qs_2.count())
