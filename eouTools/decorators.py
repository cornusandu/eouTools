from typing import Callable, Any
from functools import wraps

def rename_on_init(name: str) -> Callable:
    def decorator(func: Callable) -> Callable:
        func.__name__ = name

        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            return func(*args, **kwargs)

        return wrapper

    return decorator