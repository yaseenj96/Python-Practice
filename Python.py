# Write your code below this line 👇
print('Hello world!\nHello World!')
# \n creates a new line, and can use single quotes '' instead
print("Hello" + " Yaseen!")

# input() will get user input in console
# Then print() will print word "Hello" and user input
print("Hello" + input("what is your name?"))
# name = input()
# print("your name is" + len(name) + "characters long")

def band_name():
  print("This could be your band name!")
  city = input("What city were you born in?\n")
  pet = input("What pet do you have?\n")
  print(f"Your band name is {city} {pet}")

band_name()
