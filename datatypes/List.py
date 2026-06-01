ingredients= ["water", "milk", "black","tea"]
ingredients.append("sugar") # insert at last
print(f"Ingredients are: {ingredients}")

ingredients.remove("water")
print(f"Ingredients are: {ingredients}")

spice_options=["ginger", "cardamon"]
chai_ingredients= ["water", "milk"]

chai_ingredients.extend(spice_options)
print(f"chai: {chai_ingredients}")
chai_ingredients.insert(2, "black tea") # insert at specific index
print(f"chai: {chai_ingredients}")

last_added=chai_ingredients.pop() #remove last element of List
print(f"{last_added}")
print(f"chai: {chai_ingredients}")

chai_ingredients.reverse()
chai_ingredients.sort()

sugar_level=[1,2,3,4,5]
print(f"Maximum sugar level : {max(sugar_level)}")
print(f"Maximum sugar level : {min(sugar_level)}")
base_liquid=["water", "milk"]
extra_flavor=["ginger"]
full_liquid=base_liquid + extra_flavor
print(f"Liquid mix: {full_liquid}")

strong_brew=["black tea"]*3
print(f"String brew: {strong_brew}")

# from opewrator import itm

# Convert string to List

raw_spice_data =bytearray(b"CINNAMON")
raw_spice_data=raw_spice_data.replace(b"CINNA", b"CAD")
print(f"Bytes: {raw_spice_data}") # bytearray(b"CINNAMON")


