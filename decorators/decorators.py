from functools import wraps
def myDecorator(func):
    @wraps(func)
    def wrapper():
        
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper
    
@myDecorator
def greet():
    print("Hello from decorators class from chaicode")
    
greet()
print(greet.__name__) #wrapper but when we add @wraps it will give greet bcz it is preserving meta data