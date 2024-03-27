#!/usr/bin/env python3
"""
Implementation of redis python
"""
import uuid
import redis
from typing import Union


class Cache:
    """ A Cache class"""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
