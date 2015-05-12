# -*- coding: utf-8 -*-

from django.db.models import Avg
from rater.models import Rating


class RatingConfig(object):

    name = None
    choices = None

    def get_average_rating_for_object(self, obj):
        return Rating.objects.filter_for_object(obj).filter(
            config=self).aggregate(Avg('value'))['value__avg']


class LikeDislikeRatingConfig(RatingConfig):

    name = 'like-dislike'
    choices = (-1, 1)
