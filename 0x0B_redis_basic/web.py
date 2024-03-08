#!/usr/bin/env python3
""" Module for Implementing an expiring web cache and tracker """

from functools import wraps
import redis
import requests
from typing import Callable

r = redis.Redis()


def count_requests(method: Callable) -> Callable:
    """ Decorator for counting how many times a request has been made """

    @wraps(method)
    def wrapper(url):
        """ Wrapper for decorator functionality """
        # Increment the count
        r.incr(f"count:{url}")

        # Get the current count
        count = r.get(f"count:{url}")

        # Check if the cache is present
        cached_html = r.get(f"cached:{url}")
        if cached_html:
            return cached_html.decode('utf-8')

        # Refresh the cache and reset the count
        html = method(url)
        r.setex(f"cached:{url}", 10, html)
        r.set(f"count:{url}", 0)  # Reset the count
        return html

    return wrapper


@count_requests
def get_page(url: str) -> str:
    """ Uses the requests module to obtain the HTML
    content of a particular URL and returns it.
    """
    req = requests.get(url)
    return req.text
