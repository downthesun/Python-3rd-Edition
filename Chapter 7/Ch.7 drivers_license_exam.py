def correct_Answers():
    correct_List = ["A", "C", "A", "A", "D",
                    "B", "C", "A", "C", "B",
                    "A", "D", "C", "A", "D",
                    "C", "B", "B", "D", "A"]
    return correct_List

def open_Answers():
    answers_List = []
    
    student_Answers = open('student_solution.txt', 'r')
    
    for answer in student_Answers:
        answer = answer.rstrip('\n')
        answers_List.append(answer)
           
    return answers_List

def check(correct_List, answers_List):
    correct_Answers = 0
    
    print(correct_List) # Added for troubleshooting
    print(answers_List) # Added for troubleshooting
    
    incorrect_Answers = []

    for answer in range(0,20):
        if correct_List[answer] == answers_List[answer]:
            correct_Answers += 1    
        else:
            incorrect_Answers.append(answer + 1)
            correct_Answers += 0

    if correct_Answers < 15:
        print("Sorry! You failed the exam.")    
    else:
        print("Congratulations!! You passed the exam.")
           
    print("Number of questions you answered correctly:", correct_Answers)
    print("Number of questions you answered incorrectly:", 20 - correct_Answers)
    print("The question numbers of the incorrectly answered quesions are:",
          incorrect_Answers )
    
def main():
    correct_List = correct_Answers()
    answers_List = open_Answers()
    check(correct_List, answers_List)
    
main()
