#Arithmetic Operators
val1 = 2
val2 = 4
#Addition
add = val1 + val2
print('Addition',add)
#Sub
sub = val1 - val2
print('Subtraction',sub)
#Multiply
mul = val1 * val2
print('Multiply',mul)
#Div
div = val1 / val2
print('Division',div)
#Modulus
mod = val1 % val2
print('Modulus',mod)

# Conditional Operators
# The conditional operator ( ? : ) is used to perform an if-then or if-then-else decision. It can be thought of as
# <less than
# >greater than
# <=less than equal to
# >= great than equal to
# == equal to
# != not equal 

# Python Logical Operator
# and : returns True if both the operands are true.
# 'and' AND
# 'or' OR
# 'not' NOT 

#Logical And Operator
a = 12
b = 26
c = 17
if a>b and a>c:
    print("A Number is a largest")
if b>a and b>c:
    print("B Number is a largest")
if c>a and c>b:
    print ("C Number is a largest")


#Logical Or Operators
x = 10
y = -5
if x<0 or y<0:
    print("this is negative")
else:
    print("this is positive")

#Logical Not Operators
q = 10
if not q == 10:
    print("not equal to 10")
else:
    print("equal to 10")