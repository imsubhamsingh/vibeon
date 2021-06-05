from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models
from django.db.models.signals import pre_save

# Create your models here.


class TaggedItemManager(models.Manager):
    def unique_list(self):
        tags_set = set(self.get_queryset().values_list("tag", flat=True))
        return sorted(list(tags_set))


class TaggedItem(models.Model):
    tag = models.SlugField()

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)

    object_id = models.PositiveIntegerField()

    content_object = GenericForeignKey("content_type", "object_id")

    # def get_related_object(self):
    #     klass = self.content_type.model_class()
    #     return klass.objects.get(id= object_id)
    objects = TaggedItemManager()

    def __str__(self):
        return self.tag

    @property
    def slug(self):
        return self.tag


def lowecase_tag_pre_save(sender, instance, *args, **kwargs):
    """
    A small pre save signal to set the tags to lowercase
    so that it will correctly visible to UI
    """
    instance.tag = f"{instance.tag}".lower()


pre_save.connect(lowecase_tag_pre_save, sender=TaggedItem)
