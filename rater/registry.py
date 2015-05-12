# -*- coding: utf-8 -*-


class Registry(object):

    def __init__(self):
        self._registry = {}

    def __getitem__(self, key):
        return self._registry[key]

    def register(self, rating_config_class):
        self._registry[rating_config_class.name] = rating_config_class()

    def unregister(self, name):
        self._registry.pop(name)


registry = Registry()
