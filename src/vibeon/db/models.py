from django.db import models


class PublishStateOptions(models.TextChoices):
    # CONSTant = DB_VALUE, USER_DISPLAY_NAME
    PUBLISH = "PU", "Publish"
    DRAFT = "DR", "Draft"
    # UNLISTED = 'UN', 'Unlisted',
    # PRIVATE = 'PR', 'Private'
