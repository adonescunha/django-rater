# -*- coding: utf-8 -*-

from django.template import Library
from ..registry import registry


register = Library()


@register.filter
def average_rating(obj, rating_config_key):
    return registry[rating_config_key].get_average_rating_for_object(obj)
