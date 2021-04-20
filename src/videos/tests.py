from django.test import TestCase
from videos.models import Video
# Create your tests here.

class VideoModelTestCase(TestCase):
    def setUp(self):
        Video.objects.create(title='Scam 1992')
    
    def test_valid_title(self):
        title = 'Scam 1992'
        qs = Video.objects.filter(title=title)
        self.assertTrue(qs.exists())
    def test_created_count(self):
        title = 'Scam 1992'
        qs = Video.objects.all()
        self.assertTrue(qs.count(), 1)
