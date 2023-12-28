# Task
#     Check two given numbers and return true if one of the numbers is 50 or if their sum is 50.
#     Check from the given integer, whether it is positive or negative.
#     Check whether a given number is even or odd.
#     Check whether a given positive number is a multiple of 3.
#     All the prior tasks are to be solved with functions.
#     check from the given two numbers, weather the first number is "grater", "lesser" or "equal" to the second number.
#     check from the three sides of triangle. use conditions to determine and display 
#     weather the triangle is "Equilateral" (all sides are equal), "Isosceles" (two sides are equal), or "Scalane" (no sides are equal)
#     check from the given month (1-12) if its "Winter" (December-Feburary), "Spring" (March-May), "Summer" (June-August), or "Autumn" OR "Fall" (September-November).
#     Create a function that takes two numbers as input and returns the largest of the two.
#     create a function that takes two strings as input and returns a new string that concatenates both if them.
#     Write a function that takes a temperature in celsius and converts it to Fahrenheit.
#     Write a program that takes the age and checks if they are eligible for voting (e.g 18 or older)
#     Implement a function that checks if a given number is positive, negative, or zero and return the result.
#     create a function that takes two numbers as input and returns their product  using arithmetic operations. (e.g the product of 2 and 3 is 6)
#     implement a function that takes two strings as input and checks if they are equal.
#     Write a function that takes a number as input and returns the absolute value of the number
#     Determine whether a given year is a leap year.


# define function
a = 10
b = 20

def display():
    print(f'A is :{a} -- B is: {b}')    
    # print(a)    
# display()

# function with parametes
def display_values(a, b):
    print(f'A is : {a} -- B is : {b}')

# display_values(54, 58)

# (n(n+1))/2

# function example
def cal(n):
    result = (n * (n+1)) / 2 
    print( f'result is : { result}')

# cal(10)

# function with default values
def cal1(n=10):
    result = (n * (n+1)) / 2 
    print( f'result is : { result}')

# cal1()
# cal1(54)
# cal1(2)

# default parameter example

def circle_area(r,pi=3.14):
    result = pi * (r**2)
    print(f'Area : {result}')

# circle_area(5,3.14545321)
# circle_area(6,3.1423124)
# circle_area(45)


# funtction parameters assignment
def sum(a,b,c=20,d=25):
    print(f'A: {a} -- B: {b} -- C: {c} -- D: {d}')

# sum(1,2,54,36)
# sum(a=25,b=58,c=69,d=100)
# sum(d=100,c=69,b=58,a=25)

# sum(1,25,64)


# returning functions
def circle_area1(r,pi=3.14):
    area = pi * (r ** 2)
    return area


area = circle_area1(45)
# print(area)

# 1*2*3*4*5 =  5!



# recursive function
# def lhr():
#     print(f'A is :{a} -- B is: {b}')    
#     lhr()
# lhr()

def cal_factorial(n):

    if n == 0:
        return 1    
    else:
        return n * cal_factorial(n-1)
    
result = cal_factorial(5)
print(result)