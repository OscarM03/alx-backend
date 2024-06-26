#!/usr/bin/env python3
"""Basic Dict"""

BaseCaching = __import__('base_catching').BaseCaching


class BasicCache(BaseCaching):
    """caching system that inherits from BaseCaching"""

    def put(self, key, item):
        """Adds an item in the cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Get an item from the cache"""
        if key is None:
            return None
        value = self.cache_data.get(key)
        if value:
            return value
        return None
