flavour=["ginger", "lemon", "out of stock", "mint", "disconnected", "salty"]

for it in flavour:
    if it=="out of stock":
        continue
    if it=="disconnected":
        break
    print(f"{it} item found")

print("out of stock item found")

    