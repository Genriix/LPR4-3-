pizzas = ['pepperoni', 'cheese', 'sausage']
for pizza in pizzas:
    print(pizza)
for pizza in pizzas:
    print("I like " + pizza + " pizza.")
print("I really love pizza")

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
for my_food in my_foods:
    print(my_food)
for friend_food in friend_foods:
    print(friend_food)
my_foods.append('cannoli')
friend_foods.append('ice cream')
for my_food in my_foods:
    print(my_food)
for friend_food in friend_foods:
    print(friend_food)

dishes = ('cold appetizers', 'soups', 'hot meat dishes', 'side dishes')
for dish in dishes:
    print(dish)
dishes = ('soups', 'hot meat dishes', 'hot fish dishes', 'side dishes')
for dish in dishes:
    print(dish)
