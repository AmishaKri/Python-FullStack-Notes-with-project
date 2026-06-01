chai='Ginger chai'

def prepareChai(order):
    print("Preparing", order)
    
prepareChai(chai)
print(chai)


chai=[1,2,3]

def editChai(cup):
    cup[1]=42
    
editChai(chai)
print(chai)


def makeChai(tea, milk, sugar):
    print(tea, milk, sugar)
    
makeChai("Darjeeling", "Yes", "Low") #position args

makeChai(tea="Green", sugar="Medium", milk="No")  #kwargs

def specialChai( *ingredients,  **extras):
    print("Ingredients", ingredients)
    print("Extras", extras)
    
specialChai("Cinnamon", "Cardmon", sweetener="Honey", foam="yes")


def chaiOrder(order=[]):  # ['masala']
                          #['masala','masala']
    order.append("Masala")
    print(order)
def chaiOrder(order=None):  #[]
                            #[]
    
    if order is None:
        order=[]
        print(order)
        
chaiOrder()
chaiOrder()