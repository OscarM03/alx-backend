#!/usr/bin/env python3
"""Basic Dict"""

from base_caching import BaseCaching


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
        return self.cache_data.get(key)
