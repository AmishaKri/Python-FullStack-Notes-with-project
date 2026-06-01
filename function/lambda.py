def makeChai():
    return "Here is your masala chai"

returnValue=makeChai()
print(returnValue)

def idleChaiwala(): # None
    pass
print(idleChaiwala()) #None

def soldCups():
    return 120
total=soldCups()
print(total)

def chaiStaus(cupLeft):
    if cupLeft==0:
        return "Sorry, chai over"
    return "chai is ready"

print(chaiStaus(0))
print(chaiStaus(5))

def chaiReport():
    return 100, 20, 10 #sold, remaining

sold, remaining, z =chaiReport()
print("Sold", sold)
print("Reamianing", remaining)
