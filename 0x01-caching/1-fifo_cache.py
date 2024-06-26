#!/usr/bin/env python3
"""FIFO caching"""

from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """caching system that inherits from BaseCaching"""
    def __init__(self):
        """cache initialization"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item in the cache"""
        if key is None or item is None:
            return

        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            key1, _ = self.cache_data.popitem(False)
            print("Discard: {}".format(key1))

    def get(self, key):
        """Get an item from the cache"""
        if key is None:
            return None
        return self.cache_data.get(key)
