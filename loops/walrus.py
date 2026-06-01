value=13
remainder=value%5

if remainder:
    print(f"Not divisible, remainder is {remainder}")
    

if (remainder:=value%5):
    print(f"Not divisible, remainder is {remainder}")

size=["small", "medium", "large"]

if (request:=("choose your cup size:")) in size:
    print(f"Serving {request}")
else:
    print(f"Size is unavailable {request}")
    
    
flavours=["masala", "ginger", "lemon", "mint"]

print(f"Available flavour: {flavours}")

while(flavours:= input("Choose your flavor:")) not in flavours:
    print(f"Sorry, {flavours} is not available")

print(f"You choose {flavours} chai")