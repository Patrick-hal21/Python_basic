# Ex 1

def TriangleArea(H, W):
    Triangle = 0.5 * H * W
    return round(Triangle, 2)

Height = float(input("Entry Height: "))
Width = float(input("Entry Width: "))

print("Triangle Area = ", TriangleArea(Height, Width))
'''
def TriangleArea():
    height = input('Entry Height: ')
    base = input('Entry Base: ')
    triangle = 0.5 * float(height) * float(base)
    print('Triangle Area = ', triangle)
TriangleArea()
'''

# Ex 2

radius = float(input("Radius of circle: "))
def CircleArea(radius):
    circle_area = 3.142 * radius**2
    return round(circle_area, 2)
print("Area of the circle is ", CircleArea(radius))



# Ex 3

def TotalScore(Scores):
    total = 0
    for score in Scores:
        total += score
    return total

Scores = [56, 75, 64, 82, 77, 68]
print(Scores)
Total = TotalScore(Scores)
Average = round(Total / len(Scores), 2)
print("Total = ", Total, "Average = ", Average)


# Ex 4


def ScoreList():
    lst = []
    for x in range(5):
        lst.append(int(input("Enter Score = ")))
    return lst

def TotalScore(Scores):
    Total = 0
    for score in Scores:
        Total += score
    return Total

print("Total Score= ", TotalScore(ScoreList()))


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
                # using continue made it removed 1 score so that is imbalance with inputted number of scores
                # appending  0 makes sense to punish for inputing invalid score more than two times
                score_list.append(0)
'''
    # following code is more shorter than code used in GetScore()
'''
    def GetScore():
        num_stu = int(input("Enter number of students : "))
        num_sco = int(input("Number of scores: "))
        scores_dict = {"Student "+str(i):[int(input("Enter student's score ")) for a in range(num_sco)] for i in range(1, num_stu+1)}
        return scores_dict, num_stu, num_sco
print(GetScore())
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
def Passed(sco_dict):
    passed_stu = 0
    for i in sco_dict.values():
        count = 0
        for n in i:
            if n >= 50:
                count += 1
        if count == 3:
            passed_stu += 1
    return passed_stu

# one of inputed testscore is below 50, that student is failed
def Failed(sco_dict):
    failed_stu = 0
    for i in sco_dict.values():
        count = 0
        for n in i:
            if n < 50:
                count += 1
        if count >= 1:
            failed_stu += 1
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

start = None
option = int(input("Do you want to test program that scores and qualifies students' scores? \n 1. for Yes and 2. for No: "))
if option == 1:
    start = True
else:
    print("Completed!")

while start:
    menu()
    user_choice = int(input("Choose one option (1 - 9): "))
    if user_choice in range(1, 9):
        score_dict, num_stu, num_sco = GetScore()
        total_score = Total(score_dict)
        average_score = Average(total_score, num_sco)
        max_score, high_mark_stud = Max(total_score)
        min_score, low_mark_stud = Min(total_score)
        passed_stud = Passed(score_dict)
        failed_stud = Failed(score_dict)
        if user_choice == 2:
            print("The number of students = ", num_stu)
        elif user_choice == 3:
            print("Total score of each student = ", total_score)
        elif user_choice == 4:
            print("The average score of each student = ", average_score)
        elif user_choice == 5:
            print("Maximum score is ", max_score, " mark of ", high_mark_stud)
        elif user_choice == 6:
            print("Minimum score is ", min_score, " mark of ", low_mark_stud)
        elif user_choice == 7:
            print("The number of passed students => ", passed_stud)
        elif user_choice == 8:
            print("The number of Failed students => ", failed_stud)
    elif user_choice == 9:
        start = False
        print("Testing the program completed!")
        re_test = int(input("Do you want to retest? \n 1. for Yes and 2. for NO: "))
        if re_test  == 1:
            start = True
        else:
            print("Thanks!")
