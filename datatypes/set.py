essential_spices={"cardamon", "ginger", "cinamon"}
optional_spices={"cloves", "ginger", "black peper"}

all_spices=essential_spices|optional_spices  #union
common_spices=essential_spices & optional_spices # intersection
only_in_essential=essential_spices-optional_spices
print(f"{all_spices}")

print(f"Is 'cloves in optional spices? {'cloves' in optional_spices}")

#frozenset()


