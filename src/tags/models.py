from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models

# Create your models here.


class TaggedItem(models.Model):
    tag = models.SlugField()

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)

    object_id = models.PositiveIntegerField()

    content_object = GenericForeignKey("content_type", "object_id")

    # def get_related_object(self):
    #     klass = self.content_type.model_class()
    #     return klass.objects.get(id= object_id)
    def __str__(self):
        return self.tag
