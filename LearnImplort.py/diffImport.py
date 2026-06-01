import recipes.flavors

print(recipes.flavors.gingerChai())

from recipes.flavors import elachiChai, GingerChai
print(GingerChai())

from recipes.flavors import gingerChai
print(gingerChai())