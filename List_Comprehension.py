#List Comprehension

numbers = [1,2,3]
new_list = [n + 1 for n in numbers]

print(new_list)

name = 'Yaseen'
letters_list = [letter for letter in name]
print(letters_list)

nums = range(1,5)
range_list = [n*2 for n in nums]
print(range_list)

#Conditional List Comprehension
names = ["Alex", "Beth", "Caroline"]
short_names = [name for name in names if len(name)<5]
print(short_names)
long_names = [name.upper() for name in names if len(name)>4]
print(long_names)

#Dictionary Comprehension
import random
name = ["Alex", "Beth", "Caroline"]
students_scores = {student:random.randint(1,100) for student in names}
print(students_scores)
passed_students = {student:score for (student,score) in students_scores.items() if score>70}
print(passed_students)

#Data frame
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "scores": [45, 76, 87]
}
import pandas
student_data_frame = pandas.DataFrame(student_dict)
#Loop through rows of data frame
for (index, row) in student_data_frame.iterrows():
    print(row.student)
