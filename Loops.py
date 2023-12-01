fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
  print(fruit)
  print(fruit + "Pie")

student_score = [23, 34, 45, 23, 12]

highest_score = 0
for score in student_scores:
  if score > highest_score:
    highest_score = score

print(f"The highest score in the class is: {highest_score}")

#Range of numbers between 1 and 11, incrementing by 3
for number in range(1, 11, 3):
  print(number)

#Sum of all even numbers in range:
target = 52
sum = 0
for num in range(0, target+1):
  if num % 2 == 0:
    sum += num

#FizzBuzz
for num in range(1, 101):
  if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
  elif num % 3 == 0:
    print("Fizz")
  elif num % 5 == 0:
    print("Buzz")
  else:
    print(num)


#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
lenLetters = len(letters)
lenNumbers = len(numbers)
lenSymbols = len(symbols)
lenPassword = nr_letters + nr_symbols + nr_numbers
password = ""
# for num in range(1, nr_letters+1):
#   password += letters[random.randint(0, lenLetters-1)]

# for num in range(1, nr_symbols+1):
#   password += symbols[random.randint(0, lenSymbols-1)]

# for num in range(1, nr_numbers+1):
#   password += numbers[random.randint(0, lenNumbers-1)]


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

while len(password) < lenPassword:
  randChar = random.randint(0,2)
  if randChar == 0 and not nr_letters == 0:
    password += letters[random.randint(0, lenLetters-1)]
    nr_letters -= 1
  elif randChar == 1 and not nr_numbers == 0:
    password += numbers[random.randint(0, lenNumbers-1)]
    nr_numbers -= 1
  elif randChar == 2 and not nr_symbols == 0:
    password += symbols[random.randint(0, lenSymbols-1)]
    nr_symbols -= 1

print(password)
