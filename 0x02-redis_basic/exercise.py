#!/usr/bin/env python3
"""
Implementation of redis python
"""
import uuid
import redis
from typing import Union, Callable


class Cache:
    """ A Cache class"""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Callable = None) -> Union[str, bytes, int, float]:
        result = self._redis.get(key)
        if result is None:
            return None
        if fn is not None:
            return fn(result)
        return result

    def get_str(self, key: str) -> Union[str, None]:
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> Union[int, None]:
        return self.get(key, lambda x: int(x))
