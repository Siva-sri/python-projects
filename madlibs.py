# # string concatenation 
# # suppose we want to create a string that says "I had a _____ day"
# # mood = "great" # some string variable

# # a few ways to do this
# print("I had a" + mood + "day")
# print("I had a {} day".format(mood))
# print(f"I had a {mood} day")

# 3 method is the most efficient one

food = input("Food: ")
name = input("Name: ")
adj = input("Adjective: ")
animal = input("Animal: ")
thing = input("Thing: ")

madlib = f"It was {food} day at school, and {name} was super {adj} for lunch. \
But when she went outside to eat, a {animal} stole her {food}! \
{name} chased the {animal} all over school.Then she tripped on the {thing} and {animal} escaped! \
Luckily, {name}’s friends were willing to share their {food} with her."

print(madlib)