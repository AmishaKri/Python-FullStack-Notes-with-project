def localChai():
    yield "Masala Chai"
    yield "Ginger Chai"
    
def importChai():
    yield "Matching"
    yield "cooling"
    
def fullMenu():
    yield from localChai()
    yield from importChai()
    
    
for chai in fullMenu():
    print(chai)
    
def chaiShall():
    try:
        while True:
            order=yield "waiting for chai order"
    except:
        print("stall closed, No more chai")
        
stall=chaiShall()
print(next(stall))
stall.close()
            