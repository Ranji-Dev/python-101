student_score = input("Input a list of student score ").split()
for n in range(0,len(student_score)):
    student_score[n]= int(student_score[n])
print(student_score)
highest_score = 0
for score in student_score:
    if score > highest_score:
        highest_score = score
print(f"The highest score is {highest_score}")

#finding the highest number using max function
#print(f"The highest score is {max(student_score)}")

#finding the lowest number using min function
#print(f"The lowest score is {min(student_score)}")