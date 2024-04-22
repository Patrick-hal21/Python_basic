###
# Ex:1
# Print "Hello World" if a is greater than b
a = 50
b = 10

if a > b:
    print("Hello World")

###
# Ex : 2
# Print "Hello World" if a is not equal to  b

a = 50
b = 10 

if a != b:
    print("Hello World")

###
# Ex : 3
# Print "Yes" if a is equal to b, otherwise print "No"

a = 50
b = 10 

if a == b:
    print("Yes")
else:
    print("No")

###
# Ex : 4
# Print "1" if a is equal to b, print "2" if a is greater than b, otherwise print "3"

a = 50 
b = 10

if a == b:
    print("1")
elif a > b:
    print("2")
else:
    print("3")

###
# Ex : 5
# Print "Hello" if a is equal to b, and c is equal to d
c = 15
d = 15

if a == b and c == d:
    print("Hello")


# Print "Hello" if a is equal to b, or c is equal to d

if a == b or c == d:
    print("Hello")


###
# Ex : 6
# print "YES" if 5 is larger than 2

if 5 > 2:
    print("YES")

# print "YES" if a is equal to b, otherwise print("NO")

a = 2
b = 5

print("YES") if a == b else print("NO")

###
# Ex : 7
# print "Yes" if either a or b is equal to c

a = 2
b = 50
c = 2

if a == c or  b == c:
    print("YES")

# Ex : 8
# check whether a number is Even or Odd

print("=> To check Even or Odd...")
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Your number", num, "is Even.")
else: 
    print("Your number", num, "is Odd.")


###
#Ex : 9
# Check whther a person is eligible to vote or not in Myanmar

print("=> To check eligibilty to vote in Myanmar....")
valid_age = 18
age = int(input("Type your Age to check: "))

if age >= valid_age:
    print("You are eligible to vote.")
else:
    print("Sorry! You are ineligible to vote.")


# Ex : 10
# Calculate the area of triangle

print("=> To calculate the triangle area")
base = float(input("Enter base: "))
height = float(input("Enter height: "))
area = 0.5 * base * height
print("The resultant triangle area is " , area)


# Ex : 11

print(" => To find largest among three integers...") 
num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))
num_3 = int(input("Enter third number: "))
large_num = 0
if num_1 > num_2 and num_1 > num_3:
    large_num = num_1
elif num_2 > num_1 and num_2 > num_3:
    large_num = num_2
else:
    large_num = num_3
print(large_num, " is the largest number.")
print()

# Ex : 12
stop = False
while not stop:
    print("=> Buying tickets....")
    ticket_price = 20
    num_ticket = int(input("Type ticket amount: "))
    discount = 0
    if num_ticket >= 10 and num_ticket % 10 == 0:
        discount = ticket_price * (num_ticket / 100)
    buyable = num_ticket <= 20
    total_price = 0
    if buyable:
        total_price = (ticket_price - discount) * num_ticket
        print("It costs ", float(total_price), " .")
        stop = True
    else:
        print("Sorry! You cant't buy more than 20 tickets.")

print()

# Ex : 13

test_score = int(input("Enter your score: "))
if test_score <= 100 and test_score >= 80:
    print("You got A.")
elif test_score < 80 and test_score >= 70:
    print("You got B.")
elif test_score < 70 and test_score >= 60:
    print("You got C.")
elif test_score < 60 and test_score >= 50:
    print("You got D.")
else: 
    print("You got F.")

# Ex : 14

num_passer = int(input("Enter the number of passengers: "))
boat_capacity = int(input("Enter boat capacity: "))
num_trip = 0
if num_passer % boat_capacity == 0:
    num_trip = num_passer // boat_capacity
else:
    num_trip = num_passer // boat_capacity + 1

print("You need", num_trip, "trips to transport", num_passer, "passengers.)
print()

# Ex : 15
mark = int(input("Enter mark: "))
if mark >= 90:
    print("Your grade is A.")
elif mark < 90 and mark >= 85:
    print("Your grade is A-.")
elif mark < 85 and mark >= 80:
    print("Your grade is B+.")
elif mark < 80 and mark >= 75:
    print("Your grade is B.")
elif mark < 75 and mark >= 70:
    print("Your grade is B-.")
elif mark < 70 and mark >= 65:
    print("Your grade is C+.")
elif mark < 65 and mark >= 60:
    print("Your grade is C.")
elif mark < 60 and mark >= 55:
    print("Your grade is C-.")
elif mark < 55 and mark >= 50:
    print("Your grade is D.")
else:
    print("Your grade is F.")

