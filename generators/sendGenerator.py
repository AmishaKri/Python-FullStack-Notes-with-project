def chaiCustomer():
    print("Welcome! what chai would you like?")
    order=yield
    while True:
        print(f"Preparing: {order}")
        order=yield
    
stall=chaiCustomer()
next(stall) #start the generator


stall.send("Masala Chai")
stall.send("lemon chai")