print("Fruit kg")
kg_fruit=input()

while(kg_fruit!="end"):
    fruit_quantity=float(kg_fruit)
    water_quantity = fruit_quantity * 1.7  # it can vary between 1.2-2ltr per kg fruit depends of the fruit
    sugar_quantity = fruit_quantity / 2  # it can vary between 0.1-1kg per kg fruit depends on the sugar content  of the fruit
    print(f"Water ltr  {water_quantity}")
    print(f"Sugar kg  {sugar_quantity}")
    kg_fruit=input()


print()
print('Nice grapa!')

