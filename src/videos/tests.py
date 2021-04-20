from django.test import TestCase
from videos.models import Video, PublishStateOptions
from django.utils import timezone
from django.utils.text import slugify

# Create your tests here.


class VideoModelTestCase(TestCase):
    def setUp(self):
        self.obj_a = Video.objects.create(title="Scam 1992")
        self.obj_b = Video.objects.create(
            title="this is my title", state=PublishStateOptions.PUBLISH
        )

    def test_slug_field(self):
        title = self.obj_a.title
        test_slug = slugify(title)
        self.assertEqual(test_slug, self.obj_a.slug)

    def test_valid_title(self):
        title = "Scam 1992"
        qs = Video.objects.filter(title=title)
        self.assertTrue(qs.exists())

    def test_created_count(self):
        title = "Scam 1992"
        qs = Video.objects.all()
        self.assertTrue(qs.count(), 1)

    def test_draft_case(self):
        qs = Video.objects.filter(state=PublishStateOptions.DRAFT)
        self.assertEqual(qs.count(), 1)

    def test_publish_count(self):
        qs = Video.objects.filter(state=PublishStateOptions.PUBLISH)
        now = timezone.now()
        published_qs = Video.objects.filter(publish_timestamp__lte=now)
        self.assertTrue(published_qs.exists())

    def test_publish_manager(self):
        published_qs = Video.objects.all().published()
        published_qs_2 = Video.objects.published()
        self.assertTrue(published_qs.exists())
        self.assertEqual(published_qs.count(), published_qs_2.count())
