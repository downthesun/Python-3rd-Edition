#This program averages test scores. It asks the user for the
#number of students and the number of test scores per student.

#Get the number of students.
num_Students = int(input('How many students do you have? '))

#Get the number of test scores per student.
num_Test_Scores = int(input('How many test scores per student? '))

#Determine each student's average test score.
for student in range(num_Students):
    #Initialize an accumulator for test scores.
    total = 0.0
    #Get a studen't test scores.
    print('Student number', student + 1)
    print('-----------------')
    for test_Num in range(num_Test_Scores):
        print('Test number', test_Num + 1, end='')
        score = float(input(': '))
        #Add the score to the accumulator
        total += score

    #Calculate the average test score for this student.
    average = (total / num_Test_Scores)

    #Display the average.
    print('The average for student number', student + 1,
          'is:', average)
    print()
    
