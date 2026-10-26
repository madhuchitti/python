answer_key = ["A", "B", "C", "D", "A"]
students = ["Arun", "Bala", "Chitra"]
answers = [["A", "B", "C", "D", "A"],
    ["A", "C", "", "D", "B"],
    ["B", "B", "C", "", "A"]]
correct_mark = 2
negative_mark = 0.5
for i in range(len(students)):
    correct = 0
    incorrect = 0
    unanswered = 0
    for j in range(len(answer_key)):
        if answers[i][j] == "":
            unanswered += 1
        elif answers[i][j] == answer_key[j]:
            correct += 1
        else:
            incorrect += 1
    score = (correct * correct_mark) - (incorrect * negative_mark)
    print("Student:", students[i])
    print("Correct Answers:", correct)
    print("Incorrect Answers:", incorrect)
    print("Unanswered Questions:", unanswered)
    print("Final Score:", score)