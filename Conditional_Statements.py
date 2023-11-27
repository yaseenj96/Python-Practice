print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
  elif age >= and age <= 55:
    print("Everything is going to be okay. Have a free ride on us!")
  else:
    bill = 12
    print("Adult tickets are $12.")
  
  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo == "Y":
    bill += 3
  
  print(f"Your final bill is ${bill}")

else:
  print("Sorry, you have to grow taller before you can ride.")

weight = 80
height = 2.5

BMI = weight / height**2
if BMI < 18.5:
  output = "you are underweight."
elif BMI < 25.0:
  output = "you have a normal weight."
elif BMI < 30.0:
  output = "you are slightly overweight."
elif BMI < 35.0:
  output = "you are obese."
else:
  output = "you are clinically obese."

print(f"Your BMI is {BMI}, {output}")

firstChoice = input("Do you want to go left or right?\n")
if not firstChoice.lower() == 'left':
  print("Fall into a hole.\nGame over.")
else:
  secondChoice = input("Do you want to swim or wait?\n")
  if not secondChoice.lower() == 'wait':
    print("Attacked by trout.\nGame Over.")
  else:
    thirdChoice = input("Red, yellow, or blue door?\n")
    if thirdChoice.lower() == 'red':
      print("Burned by fire. Game Over.")
    elif thirdChoice.lower() == 'blue':
      print("Eaten by beasts. Game Over")
    elif thirdChoice.lower() == 'yellow':
      print("You Win!")
    else:
      print("Game Over.")
