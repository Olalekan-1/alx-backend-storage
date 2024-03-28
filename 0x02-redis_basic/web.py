#!/usr/bin/env python3
"""
Implementation of redis python
"""

import requests
import redis
import time


def get_page(url: str) -> str:
    """ get page function """
    redis_conn = redis.Redis()

    count_key = f"count:{url}"
    access_count = redis_conn.get(count_key)
    if access_count:
        redis_conn.incr(count_key)
    else:
        redis_conn.set(count_key, 1)
        redis_conn.expire(count_key, 10)
    response = requests.get(url)
    html_content = response.text

    return html_content
