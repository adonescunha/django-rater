# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings
from rater.fields import RatingConfigReferenceField


class Rating(models.Model):

    user = models.ForeignKey(getattr(settings, 'AUTH_USER_MODEL', 'auth.User'))
    rated_object_id = models.PositiveIntegerField()
    rated_object_type = models.ForeignKey(ContentType)
    rated_object = GenericForeignKey(
        'rated_object_type',
        'rated_object_id')
    config = RatingConfigReferenceField()
    value = models.IntegerField()
    message = models.TextField(null=True, blank=True)
