# Ex 1

print("=======> Ex : 1")
i = 1
while i < 6:
    print(i)
    i += 1

# Ex 2

print("=======> Ex : 2")
i = 1
while i < 6:
    if i == 3:
        break
    i += 1

# Ex 3

print("=======> Ex : 3")
i = 1
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)


# Ex 4

print("=======> Ex : 4")
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

# Ex 5
# print a message once the condition is false

print("=======> Ex : 5")
fruits = ["apple", "banana", "cherry"]
for x  in fruits[3:]:
    print(x)


# Ex 6
# Loop through items in fruits list

print("=======> Ex : 6")
fruits = ["apple", "banana", "cherry"]
for x  in fruits:
    print(x)


# Ex 7

print("=======> Ex : 7")
fruits = ["apple", "banana", "cherry"]
for x  in fruits:
    if x == "banana":
        continue
    print(x)


# Ex 8

print("=======> Ex : 8")
for x in range(10):
    print(x)


# Ex 9

print("=======> Ex : 9")
fruits = ["apple", "banana", "cherry"]
for x  in fruits:
    if x == "banana":
        break
    print(x)


# Ex 10
# Fibonacci

start = True
def fibonacci_seri(num_fibo_seri):
    
    # Fibonacci sereis always start with 0 and 1
    n = num_fibo_seri - 2
    fibonacci = [0, 1]
    for i in range(n):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    print(fibonacci)

while start:
    print("=======> Ex : 10")
    num_fibo_seri = int(input("Enter number of Fibonacci series you want: "))
    fibonacci_seri(num_fibo_seri) 

    choice = str(input("Do you want find some more? (y or n): ")).lower()
    if choice ==  "n":
        start = False

print(">>>>>   Completed!   <<<<<")