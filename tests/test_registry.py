# -*- coding: utf-8 -*-

from django.test import TestCase
from rater.registry import Registry


class DummyConfig(object):

    name = 'dummy-rating'


class RegistryTests(TestCase):

    def setUp(self):
        self.registry = Registry()

    def test_registry_is_assigned_when_initialized(self):
        self.assertEqual(self.registry._registry, {})

    def test_get_item_is_delegated_to_registry(self):
        key = 'key'
        value = 'value'
        self.registry._registry[key] = value
        self.assertEqual(self.registry[key], value)

    def test_register(self):
        name = DummyConfig.name
        self.registry.register(DummyConfig)
        self.assertTrue(self.registry._registry.has_key(name))
        self.assertIsInstance(self.registry[name], DummyConfig)

    def test_unregister(self):
        name = DummyConfig.name
        self.registry.register(DummyConfig)
        self.assertTrue(self.registry._registry.has_key(name))
        self.registry.unregister(name)
        self.assertFalse(self.registry._registry.has_key(name))
