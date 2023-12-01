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
