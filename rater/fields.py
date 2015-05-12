# -*- coding: utf-8 -*-

from django.db import models
from .registry import registry


def get_rating_config(rating_config_name):
    return registry[rating_config_name]


class RatingConfigReferenceField(models.CharField):

    __metaclass__ = models.SubfieldBase

    def to_python(self, value):
        if isinstance(value, basestring) and value:
            return get_rating_config(value)

        return value

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_prep_value(value)

    def get_prep_value(self, value):
        if value is None:
            return None

        return value.name
