# app/services/decorators.py

import functools
import time

def log_inference(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start_time
        print(f"[LOG] Функция '{func.__name__}' выполнена за {duration:.3f} сек.")
        return result
    return wrapper
