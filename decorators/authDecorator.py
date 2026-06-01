from functools import wraps

def requireAdmin(func):
    @wraps(func)
    def wrapper(user):
        if user!="admin":
            print("Access denied: Admins only")
            return None
        else:
            return func(user)
    return wrapper

@requireAdmin
def accessTea(role):
    print("Access granted to tea investory")
    
accessTea('user')
accessTea('admin')
        