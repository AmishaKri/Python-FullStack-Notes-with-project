menu=[
    "Ginger chai",
    "Iced Lemon Tea", 
    "Green Tea",
    "Iced Peach Tea",
    "Masala Tea"
]

icedTea=[myTea for myTea in menu if len(myTea)<12]

print(icedTea)