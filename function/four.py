def calculateBills(cups, pricespercup):
    return cups*pricespercup

total=calculateBills(13, 5)
print(f"{total}")

print("Order for table 2:", calculateBills(15, 5))

def brewChai(type, milk="no"):
    print(f"brewing {type} chai and milk status {milk}")
    
brewChai("Masala")