class chai:   #attribute shallowing
    temperature="hot"
    strength="Strong"
    
cutting=chai()
print(cutting.temperature)

cutting.temperature="mild"
cutting.cup="small"
print("After changing", cutting.temperature)
print("Direct look into the class", chai.temperature)

del cutting.temperature
del cutting.cup
print(cutting.temperature)
print(cutting.cup)  #error no attribute

