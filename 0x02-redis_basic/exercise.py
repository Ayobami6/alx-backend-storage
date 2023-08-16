#!/usr/bin/env python3
""" python redis practice scripts """
import redis
from uuid import uuid4
from typing import Union


class Cache:
    """ Cache Storage class
    """

    def __init__(self) -> None:
        self._redis: redis.Redis = redis.Redis()  # Redis client instance
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        key: str = str(uuid4())  # Generate a unique key
        self._redis.set(key, data)  # Store the data in Redis
        return key  # Return the key for later retrieval
