from functools import wraps
def logActivity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"calling: {func.__name__}")
        result=func(*args, **kwargs)
        print(f"calling: {func.__name__}")
        return result
    return wrapper

@logActivity
def brewChai(type, milk="no"):
    print(f"brewing {type} chai and milk status {milk}")
    
brewChai("Masala")