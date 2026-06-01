def pureChai(cups):
    return cups *10

ans=pureChai(5)
print(ans)
totalChai=0

# not recommended

def impureChai(cups):
    global totalChai
    totalChai+=cups
    return totalChai
result=impureChai(5)
print(result)

#Recursive function

def pourChai(n):
    print(n)
    if n==0:
        return "All cupes poured"
    return pourChai(n-1)

    
anns=pourChai(8)
print(pourChai(8))

#Lambdas Function
chaiType=["light", "ginger", "kadak","kadak", "mint"]

strongChai=list(filter(lambda chai: chai!="kadak", chaiType))
print(strongChai)
