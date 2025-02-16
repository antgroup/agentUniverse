# !/usr/bin/env python3
# -*- coding:utf-8 -*-

import functools
import time
from typing import Any, Callable


def retry(max_retries: int = 3, delay: float = 1.0) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            retries = 0
            last_exception = None
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    retries += 1
                    if retries < max_retries:
                        time.sleep(delay)                    
            raise Exception(f"Failed after {max_retries} retries. Last error: {str(last_exception)}")
        return wrapper
    return decorator
