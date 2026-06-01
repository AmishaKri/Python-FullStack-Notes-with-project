def addVat(price, vatRate):
    return price*(100+vatRate)/100


orders=[100, 150, 200]

for price in orders:
    finalAmount=addVat(price, 10)
    print(f"Original: {price}, final with VAT: {finalAmount}")