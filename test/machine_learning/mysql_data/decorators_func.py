from functools import wraps
def decorator_factory(param):
    def outer(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if param['isIni']:
                param['isIni']=False
                return func(*args, **kwargs)  # Call hello
        return wrapper
    return outer