# Ex 5

def GetScore():
    num_stu = int(input("Number of students: "))
    num_sco = int(input("Number of scores: "))
    scores_dict ={}
    for i in range(1, num_stu+1):
        if i not in scores_dict.keys():
            print("==> For student", i)
            scores_dict["Student "+ str(i)] = [int(input("Enter student's score (0-100): ")) for a in range(num_sco)]
    return scores_dict, num_stu, num_sco
    # following code will make inputted score in range(0-100) ,and 
    # entering score is limited to 2 attempt to make it valid which is in range(0-100)
'''
    score_lst = []
    for i in range(num_score):
        score = int(input(" Enter your score: "))
        if score >= 0 and score <= 100:
            score_list.append(score)
        else:
            new_score = int(input("Invalid input! \n Be careful! \n Enter your score one last again: "))
            if new_score >= 0 and new_score <= 100:
                score_list.append(new_score)
            else:
                continue
'''
def Total(sco_dict):
    total = {}
    for i, j in sco_dict.items():
        if i not in total.keys():
            total[i] = 0
            for n in j:
                total[i] += n
    return total
# print(Total(stu_score_dict))
def Average(total_dict, num_sco):
    average = {}
    for i, j in total_dict.items():
        if i not in average.keys():
            # for visual, I rounded the value to two decimal point
            average[i] = round(j / num_sco, 2)
    return average

def Max(total_dict):
    max_score = 0
    high_mk_stu = ""
    for i, j in total_dict.items():
        if j > max_score:
            max_score = j
            high_mk_stu = i
    return max_score, high_mk_stu

def Min(total_dict):
    min_score = None
    low_mk_stu = ''
    for i, j in total_dict.items():
        if min_score is None or j < min_score:
            min_score = j
            low_mk_stu = i
    return min_score, low_mk_stu

# if only all of the inputed testscores are above or equal 50,
# that student is passed
def Passed(sco_dict, num_sco):
    passed_stu = 0
    for i in sco_dict.values():
        count = 0
        for n in i:
            if n >= 50:
                count += 1
        if count == num_sco:
            passed_stu += 1
    return passed_stu

# one of inputed testscore is below 50, that student is failed
def Failed(sco_dict, num_stu, num_sco):
    failed_stu = num_stu - Passed(sco_dict, num_sco)

    # this is with 1 parameter
    # failed_stu = 0
    # for i in sco_dict.values():
    #     count = 0
    #     for n in i:
    #         if n < 50:
    #             count += 1
    #     if count > 0:
    #         failed_stu += 1
    return failed_stu
# testing functions
'''
stu_score_dict, num_stu, num_sco = GetScore()
total_score = Total(stu_score_dict)
average_score = Average(total_score, num_sco)
max_score, high_mark_stud = Max(total_score)
min_score, low_mark_stud = Min(total_score)
passed_stud = Passed(stu_score_dict)
failed_stud = Failed(stu_score_dict)

print("Total scores are => ", total_score)
print("Average scores are => ", average_score)
print("Max score => ", max_score, " mark of ", high_mark_stud)
print("Min score => ", min_score, " mark of ", low_mark_stud)
print("The number of passed students => ", passed_stud)
print("The number of failed students => ", failed_stud)
'''

# Ex 6

def menu():
    print("\n Options for you...")
    print("1.  To input students' scores")
    print("2.  To display number of students")
    print("3.  To display Total score")
    print("4.  To display Average score")
    print("5.  To display Maximun score")
    print("6.  To display Minimum score")
    print("7.  To display Number of students who Passed the exam")
    print("8.  To display Number of students who Failed the exam")
    print("9.  Exit program")
    # option = int(input("Do you want to continue? \n 1. for Yes and 2. for No: "))
    # if option == 1:
    #     start = True
    # else:
    #     print("Completed!")
    #     start = False

start = True
# option = int(input("Do you want to continue? \n 1. for Yes and 2. for No: "))
# if option == 1:
#     start = True
# else:
#     print("Completed!")
#     start = False

while start:
    menu()
    user_choice = int(input("Choose one option (1 - 9): "))
    if user_choice == 1:
        score_dict, num_stu, num_sco = GetScore()
        total_score = Total(score_dict)
        average_score = Average(total_score, num_sco)
        max_score, high_mark_stud = Max(total_score)
        min_score, low_mark_stud = Min(total_score)
        passed_stud = Passed(score_dict, num_sco)
        failed_stud = Failed(score_dict, num_stu, num_sco)
    if user_choice == 2:
        print("\n ==> The number of students = ", num_stu)
    elif user_choice == 3:
        print("\n ==> Total score of each student -")
        print(*(f"\n\t{s} = {m}" for s, m in total_score.items()))
    elif user_choice == 4:
        print("\n ==> The average score of each student -")
        print(*(f"\n\t{s} = {m}" for s, m in average_score.items()))
    elif user_choice == 5:
        print(f"\n ==> {max_score} total score of {high_mark_stud} is Maximum score among {num_stu} students.")
    elif user_choice == 6:
        print(f"\n ==> {min_score} total score of {low_mark_stud} is Minimum score among {num_stu} students.")
    elif user_choice == 7:
        print("\n ==> The number of passed students => ", passed_stud)
    elif user_choice == 8:
        print("\n ==>The number of Failed students => ", failed_stud)
    elif user_choice == 9:
        start = False
        print("\n >>> Testing the program completed! <<< \n")
        re_test = int(input("Do you want to restart? \n 1. for Yes | 2. for NO: "))
        if re_test  == 1:
            start = True
        else:
            print("Thanks!")
        