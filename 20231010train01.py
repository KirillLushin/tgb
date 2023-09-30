shopping_list = ["potato", "apple", "oil", "milk", "toilet paper"]
shopping_list.append("batteries")
shopping_list.insert(0, "chocolate")
shopping_list[0] = "dark chocolate"
shopping_list.pop()
purchased_list = ["dark chocolate", "potato", "apple", "oil", "toilet paper", "fish fingers"]
unavailable_items = []
for item in shopping_list:
  if item not in purchased_list:
     unavailable_items.append(item)

print (shopping_list)
print (purchased_list)
print (unavailable_items)
