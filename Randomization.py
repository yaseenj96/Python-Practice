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

# len() length function
names = ["Ben", "Jesse", "Joy"]
length = len(names)
randomint = random.randint(0, (length-1))
print(f"{names[randomint]} is going to buy the meal today!")

# Double indexing (indexing lists)
line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# Your code below
letter = position[0].lower()
abc = ["a", "b", "c"]
letter_index = abc.index(letter)
number_index = int(position[1]) - 1
map[number_index][letter_index] = "X"

print(f"{line1}\n{line2}\n{line3}")
