#!/usr/bin/env python3
"""FIFO caching"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """caching system that inherits from BaseCaching"""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Adds an item in the cache"""
        if key is None or item is None:
            return

        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            key1 = next(iter(self.cache_data))
            print("Discard: {}".format(key1))
            del self.cache_data[key1]

    def get(self, key):
        """Get an item from the cache"""
        if key is None:
            return None
        return self.cache_data.get(key)
