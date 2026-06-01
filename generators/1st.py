# Generators  word always we see yield

#you save memory ... you don't want the results immediately ... lazy evaluation


def saveChai():
    yield "Cup 1: Masala Chai"
    yield "Cup 2: Ginger Chai"
    yield "Cup 3: Elaichi Chai"

stall=saveChai()
# for cup in stall:
#     print(cup)
    
def getChai():
    return ["Cup 1", "Cup 2", "Cup 3"]

#generate function

def getChai():
    yield "Cup 1: Masala Chai"
    yield "Cup 2: Ginger Chai"
    yield "Cup 3: Elaichi Chai"
    
chai=getChai()
print(next(chai))
print(next(chai))
print(next(chai))
print(next(chai)) #error
 