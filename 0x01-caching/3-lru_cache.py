#!/usr/bin/env python3
"""LRU caching"""

from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """caching system that inherits from BaseCaching"""
    def __init__(self):
        """cache initialization"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item in the cache"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data.move_to_end(key)

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            key1, _ = self.cache_data.popitem(False)
            print("Discard:", key1)

    def get(self, key):
        """Get an item from the cache"""
        if key is None or key not in self.cache_data:
            return None
        self.cache_data.move_to_end(key)

        return self.cache_data.get(key)
