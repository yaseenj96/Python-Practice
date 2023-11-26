print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:
  print("You can ride the rollercoaster!")
else:
  print("Sorry, you have to grow taller before you can ride!")

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
