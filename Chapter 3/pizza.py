#4-1 Pizzas
pizzas = ["Pepporoni", "Cheese", "Hawaiian", "Philly", "Smoked Mozzerella"]
for pizza in pizzas:
	print ("I like " + pizza + " pizza.")
print('I really love pizza')

#4-2 Animals
animals = ["Penguins", "Chickens", "Flamingos"]
for animal in animals:
	print(animal + " are a bird.")
print("All of these animals are birds.")

#4-10 Slices
print("The first three items in the list are:")
for pizza in pizzas[:3]:
	print(pizza)
print("The middle three items in the list are:")
for pizza in pizzas[1:4]:
	print(pizza)
print("The last three items in the list are:")
for pizza in pizzas[-3:]:
	print(pizza)
	
#4-11 My Pizzas, Your Pizzas
friend_pizzas = pizzas[:]
pizzas.append("Meat")
friend_pizzas.append("Everything")
print("My favorite pizzas are ")
for pizza in pizzas:
	print(pizza + " ")
print("My friend's favorite pizzas are ")
for pizza in friend_pizzas:
	print(pizza + " ")

#4-12 More Loops
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are: ")
for food in my_foods:
	print(food + " ")
print("\nMy friend's favorite foods are: ")
for food in friend_foods:
	print(food + " ")