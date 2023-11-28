import random
# import my_module

c = random.randint(100,200) 
# Randint returns a random number between two inputs
rand_float = random.random()*5
# Random outputs random float
print(c)
# print(my_module.pi)
print(rand_float)


# Lists and List Methods
list = [1, 2, 3]
list[1] = "two"
print(list)
list.append("four")
print(list)
list.extend([5, 6, 7])
print(list)
list.reverse()
print(list)
list.insert(1, "thisIs2")
print(list)
