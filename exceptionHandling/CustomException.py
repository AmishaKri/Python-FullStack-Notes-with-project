class UnknownFlavorError(Exception):
    pass

def brewChai(flavor):
    if flavor not in ["masala", "ginger", "elaichi"]:
        raise UnknownFlavorError(f"Unknown flavor: {flavor}")
    print(f"Brewing {flavor} chai")
    
try:
    brewChai("mint")
except UnknownFlavorError as e:
    print(f"Error: {e}")
    print("Available flavors: masala, ginger, elaichi")


class OutOfIngredientError(Exception):
    pass

def makeChai(milk, sugar):
    if milk ==0 or sugar == 0:
        raise OutOfIngredientError("Out of ingredients")
    print(f"Making chai with {milk} milk and {sugar} sugar")
    