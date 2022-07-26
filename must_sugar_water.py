print("Fruit kg")
kg_fruit=input()
print("Fruit type")
type_fruit=input()

while(kg_fruit!="end"):
    fruit_quantity=float(kg_fruit)
    if type_fruit=="grape":
        water_quantity = fruit_quantity * 1  # it can vary between 1.2-2ltr per kg fruit depends of the fruit
        sugar_quantity = fruit_quantity / 1  # it can vary between 0.1-1kg per kg fruit depends on the sugar content  of the fruit
        print(f"Water   {water_quantity} ltr")
        print(f"Sugar   {sugar_quantity} kg")
    elif type_fruit=="plum":
        water_quantity = fruit_quantity * 1.7  # it can vary between 1.2-2ltr per kg fruit depends of the fruit
        sugar_quantity = fruit_quantity / 2  # it can vary between 0.1-1kg per kg fruit depends on the sugar content  of the fruit
        print(f"Water   {water_quantity} ltr")
        print(f"Sugar   {sugar_quantity} kg")
    elif type_fruit=="apricot":
        water_quantity = fruit_quantity * 1.7  # it can vary between 1.2-2ltr per kg fruit depends of the fruit
        sugar_quantity = fruit_quantity / 2  # it can vary between 0.1-1kg per kg fruit depends on the sugar content  of the fruit
        print(f"Water   {water_quantity} ltr")
        print(f"Sugar   {sugar_quantity} kg")
    elif type_fruit=="fig":
        water_quantity = fruit_quantity * 2  # it can vary between 1.2-2ltr per kg fruit depends of the fruit
        sugar_quantity = fruit_quantity / 2.2  # it can vary between 0.1-1kg per kg fruit depends on the sugar content  of the fruit
        print(f"Water   {water_quantity} ltr")
        print(f"Sugar   {sugar_quantity} kg")
    elif type_fruit == "mulberry":
        water_quantity = fruit_quantity * 1.7  # it can vary between 1.2-2ltr per kg fruit depends of the fruit
        sugar_quantity = fruit_quantity / 2  # it can vary between 0.1-1kg per kg fruit depends on the sugar content  of the fruit
        print(f"Water   {water_quantity} ltr")
        print(f"Sugar   {sugar_quantity} kg")
    elif type_fruit == "pear":
        water_quantity = fruit_quantity * 1.7  # it can vary between 1.2-2ltr per kg fruit depends of the fruit
        sugar_quantity = fruit_quantity / 2  # it can vary between 0.1-1kg per kg fruit depends on the sugar content  of the fruit
        print(f"Water   {water_quantity} ltr")
        print(f"Sugar   {sugar_quantity} kg")
    else:
        water_quantity = fruit_quantity * 1.7  # it can vary between 1.2-2ltr per kg fruit depends of the fruit
        sugar_quantity = fruit_quantity / 2  # it can vary between 0.1-1kg per kg fruit depends on the sugar content  of the fruit
        print(f"Water   {water_quantity} ltr")
        print(f"Sugar   {sugar_quantity} kg")
    kg_fruit=input()



print()
print('Nice grapa!')

