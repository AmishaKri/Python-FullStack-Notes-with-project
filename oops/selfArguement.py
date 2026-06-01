class chaiCup:
    size= 150
    
    def describe(self):
        return f"A {self.size} ml chai cup"
    
cup=chaiCup()
print(cup.describe())
print(chaiCup.describe(cup))  #self arguement

cupTwo=chaiCup()
cupTwo.size=100
print(chaiCup.describe(cupTwo))