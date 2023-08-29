#Task 1
three_mul = 'fizz'
five_mul = 'buzz'
num1 = 3
num2 = 4 
max_num = 100
   
for i in range(1,max_num):
    # % or modulo division gives you the remainder 
    
    if i%num1 == 0:
        print(i, three_mul)
    elif i%num2 == 0:
        print(i, five_mul)
    elif i%num1 == 0 and i%num2 == 0:
        print(i, three_mul+five_mul)

#Task2

n = 5
number = 1
sum = 0
while number < n + 1:
    sum = sum + number
    number = number + 1
print("Sum =", sum)


# Task 3

n = 5
sum = 0
for num in range(n):
    sum +=  n - num
print("Sum =", sum)


#Task 4
#No 1
for x in range(3):
    print(x)

#No 2
for j in range(5):
    print(j)

#No 3
x = 10
while x > 0:
    print(x)
    x -= 1

#No4
countdown = 5
while countdown > 0:
    print(f"{countdown}")
    countdown -= 1

print("Start!")


#Task 5

x = int(input("First number: "))
y = int(input("Second number: "))
z = int(input("Third number: "))

if x == y or y == z:
    sum = 0
else:
    sum = x + y + z
print("Calculated sum is ", sum)

#Task 6

x = int(input("First number: "))
y = int(input("Second number: "))

sum = x + y

if sum > 15 and sum < 20:
    result = 20
else:
    result = sum    
print("Calculated sum is ", result)

#Task 7


a = input("First value: ")
b = input("Second value: ")

print("Before swapping: a =", a, " b =", b)

a, b = b, a

print("After swapping: a =", a, " b =", b)

#Task 8
x = int(input("First number: "))
y = int(input("Second number: "))
z = int(input("Third number: "))

print("The maximum value is ", float(max(x, y ,z)))
print("The minimum value is ", float(min(x, y ,z)))

# Task 9
x = input("Type your value: ")

if x == "0":
    x = "false"
elif x == "1":
    x = "true"
else:
    x
print("Your entered value is now ", x)

#Task 10

x = int(input("First number: "))
y = int(input("Second number: "))

if y % x == 0:
    result = y // x
    print("Second number is divisible by first number, result =", result)
elif x % y == 0:
    result = x // y
    print("First number is divisible by second number, result =", result)
else:
    print("Numbers are not divisible!")
