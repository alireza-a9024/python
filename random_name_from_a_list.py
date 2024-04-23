import random
names_string = input("Enter names separated by a space: ")
names = names_string.split(" ")
print(names)
rand_names = names[random.randint(0, len(names)-1)]
print(rand_names)

# or we can use random.choice

pick_name = random.choice(names)
print(pick_name)
