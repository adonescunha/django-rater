# -*- coding: utf-8 -*-

from django.test import TestCase
from rater.fields import RatingConfigReferenceField
from rater.registry import registry


class DummyConfig(object):

    name = 'dummy-rating'


class RatingConfigReferenceFieldTests(TestCase):

    def setUp(self):
        self.field = RatingConfigReferenceField()

    def test_get_prep_value_returns_none_when_value_is_none(self):
        self._test_get_prep_value(None, None)

    def test_get_prep_value_returns_value_name(self):
        value = DummyConfig()

        self._test_get_prep_value(value, DummyConfig.name)

    def test_to_python_returns_value_when_value_is_not_a_basestring(self):
        value = 123

        self.assertEqual(self.field.to_python(value), value)

    def test_to_python_returns_a_rating_config_when_values_is_a_basestring(self):
        registry.register(DummyConfig)
        self.assertIsInstance(self.field.to_python(DummyConfig.name),
                              DummyConfig)

    def _test_get_prep_value(self, value, expected):
        self.assertEqual(self.field.get_prep_value(value), expected)
