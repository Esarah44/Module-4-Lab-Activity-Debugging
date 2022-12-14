# Program Name: grading.py
# Purpose of a program:
# Write a program computing an average of three exam scores
# User enters three exam scores.
# Program prints the exam scores, average of three scores, corresponding letter grade,
# and result of Pass or Fail of a course.


# To pass a course, student should get a grade C or above.

# Average Score    Grade
#    90+	        A
#    80-89	        B
#    70-79	        C
#    60-69	        D
#    0-59	        F

# Example of output
# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.


exam_one = int(input("Input exam grade one: "))

exam_two = int(input("Input exam grade two: "))

#exam_three = int(input("Input exam grade three: "))
exam_three = str(input("Input exam grade three: "))

grades = [exam_one, exam_two, exam_three]
total = 0

#Change type should be done before computing.
#for grade in grades:
#     total = total + grade

for grade in grades:
     total = int(total) + int(grade)

avg = total / len(grades)

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90:
    letter_grade = "B"
elif avg >= 70 and avg < 80:
    letter_grade = "C"
elif avg >= 60 and avg < 70:
    letter_grade = "D"
elif avg >= 0 and avg < 60:     
    letter_grade = "F"
#if-elif-else 
#else:
#     print("Invalid Grade")
for grade in grades:
    print("Exam: " + str(grade))
#No indentation because grade and average should be printed once.
#print("Average: " + str(avg))
#print("Grade: " + letter_grade)
    print("Average: " + str(avg))

    print("Grade: " + letter_grade)

if letter_grade == "F":
    print ("Student is failing.")
else:
    print ("Student is passing.")
