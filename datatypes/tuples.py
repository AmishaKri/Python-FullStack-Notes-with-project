masala_spices=("cardamon", "cloves", "cinnamon")

(spices1, spices2, spices3)=masala_spices
print(f"Main masala: {spices1}, {spices2}, {spices3}")

ginger_ratio, cadramom_ratio = 2,1
print(f"Ratio is G{ginger_ratio} and C: {cadramom_ratio}")
# Swap variables
ginger_ratio, cadramom_ratio=cadramom_ratio, ginger_ratio
print(f"Ratio is G{ginger_ratio} and C: {cadramom_ratio}")

#membership
print(f"Is ginger in masala spices?{'ginger'in masala_spices}") # False
print(f"Is ginger in masala spices?{'cadramon'in masala_spices}")# True
print(f"Is ginger in masala spices?{'Cadramon'in masala_spices}") # False bcz Case sensitive
