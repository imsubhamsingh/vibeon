from django.utils import timezone
from django.utils.text import slugify
from videos.models import PublishStateOptions


def publish_state_pre_save(sender, instance, *args, **kwargs):
    is_publish = instance.state == PublishStateOptions.PUBLISH
    is_draft = instance.state == PublishStateOptions.DRAFT
    if is_publish and instance.publish_timestamp is None:
        instance.publish_timestamp = timezone.now()
    elif is_draft:
        instance.publish_timestamp = None


def slugify_pre_save(sender, instance, *args, **kwargs):
    title = instance.title
    if instance.slug is None:
        instance.slug = slugify(instance.title)
