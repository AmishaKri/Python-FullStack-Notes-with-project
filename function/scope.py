def serveChai():
    chaiType="masala"  #local scope
    print(f"Inside function {chaiType}")
    
chaiType="Lemon"
serveChai()
print(f"Outside function: {chaiType}")

def chaiCount():
    chaiOrder="lemon" #Enclosing scope
    
    def printOrder():
        chaiOrder="ginger"
        print("Inner:", chaiOrder)
    printOrder()
    print("Outer:", chaiOrder)