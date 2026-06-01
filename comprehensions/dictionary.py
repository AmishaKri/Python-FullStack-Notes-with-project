#Python comprehensions (like list, dict, and set comprehensions) are used to make code shorter, cleaner, and faster when creating collections.

teaPrices={
    "Masala Chai": 40,
    "Green Tea": 50,
    "Lemon Tea": 70
}

TeaPrice={tea:price/80 for tea, price in teaPrices.items()}
print(TeaPrice)