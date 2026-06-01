menu={
    "Ginger chai",
    "Iced Lemon Tea", 
    "Green Tea",
    "Iced Peach Tea",
    "Masala Tea",
    "Ginger chai"
}

icedTea={myTea for myTea in menu if len(myTea)<12}

print(icedTea)

receipes={
    "Masala Chai":["ginger", "cardamon", "clover"], 
    "Elaichi Chai": ["cardamon", "milk"],
    "Spicy Chai": ["ginger", "black pepper", "clover"]
}

unique={spices for ingredients in receipes.values() for spices in ingredients}
print(unique)