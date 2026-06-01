chai_order=dict(type="Masala Chai", size="Large", sugar=2)
print(f"Chai order: {chai_order}")

chai_recipe={}
chai_recipe["base"]="black tea"
chai_recipe["liquid"]="liquid tea"

del chai_recipe["liquid"]

print(f"Is sugar in the order? {'sugar' in chai_order}")


chai_order={"type":"Ginger chai", "size":"Meduim", "sugar":1}
print(f"Order details (keys): {chai_order.keys()}")
print(f"Order details (values): {chai_order.values()}")
print(f"order details(items): {chai_order.items()}")

last_item=chai_order.popitem()
print(f"Removed last: {last_item}")

extra_spices={"cardamom":"crushed", "ginger":"sliced"}
chai_recipe.update(extra_spices)
print(f"Removed last: {chai_recipe}")
customer_note=chai_order.get("size", "No Note")