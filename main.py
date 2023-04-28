# Import the Food class and Drink class
from menu_item import MenuItem
from food import Food
from drink import Drink

# Create an instance of the Food class and assign it to the food variables
food1 = Food('Sandwich', 5, 330)
food2 = Food('Chocolate Cake', 4, 450)
food3 = Food('Cream Puff', 2, 180)

foods = [food1, food2, food3]

# Create an instance of the Drink class and assign it to the drink variables
drink1 = Drink('Coffee', 3, 180)
drink2 = Drink('Orange Juice', 2, 350)
drink3 = Drink('Espresso', 3, 30)

drinks = [drink1, drink2, drink3]

print('Food')
index = 0
# Call the info method from foods and output the return value
for food in foods:
    print(str(index) + '. ' + food.info())
    index += 1

print('Drinks')
index = 0
# Call the info method from drinks and output the return value
for drink in drinks:
    print(str(index) + '. ' + drink.info())
    index += 1

print('--------------------')

food_order = int(input('Enter food item number: '))
selected_food = foods[food_order]

drink_order = int(input('Enter drink item number: '))
selected_drink = drinks[drink_order]


# Take input from the console and assign it to the count variable
count = int(input("How many meals would you like to purchase? (10% off for 3 or more): "))

# Call the get_total_price method from selected_food and from selected_drink
result = selected_food.get_total_price(count) + selected_drink.get_total_price(count)

# Output 'Your total is $____'
print("Your total is $"+str(result))