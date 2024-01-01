print('python Loops')
''' 
Sum all the list elements by using both a loop and a Python built-in function.
Reverse the list by using both a loop and a Python built-in function.
Make a table of the given number with all possible loops.
Find the largest number in a list by using both a loop and a Python built-in function.
Find the smallest number in a list by using both a loop and a Python built-in function.
Add the list element at the specified index.
Delete the list element from the specified index.
Make a normal list to store the name of 5 students and iterate with for and foreach loop.
Make an associative list to store the name of 5 students and iterate with a foreach loop.
Make a normal list of associative Lists(a list that will have associative Lists) to store the information of at least 2 students and access them as hard-coded.
Information to store:
Name, age, registration number, course, favorite programming languages (should be a    normal list), Marks of 5 different subjects (should be an associative list).
The operations to perform:
Display every single value for any student.
Display the first and last favorite programming languages of any student.
Display the marks of any two subjects for any student.


'''



# for loop
# single parameter
# for i in range(10):
#     print(i)

# two parameters
# function overloading
# for i in range(5,11):
#     print(i)

# 3 parameters
# for i in range(0,20,2):
#     print(i)

# reverse loop
# for i in range(20,0,-3):
#     print(i)

# loop on list
names = ['Ahamd','Ali','Sultan','Umar','Usman','Farhat','Alizay','Akbar','Babloo']
# for name in names:
#     print(name)
# print(names)

# get index and values from list
for name in enumerate(names):
    print(f" index : {name[0]} -- Value : {name[1]}" )
    # print(name)

for index, value  in enumerate(names):
    print(f'Index is : {index} -- Value is: {value}')

dic = {
    'fname' : 'ahmad',
    'lname' : 'ali',
    'course' : 'python',
    'age' : 25,
    'email' : 'ahmadali@gmail.com',
    'phone' : '030012345678'
}

for i in enumerate(dic):
    print(f"index : {i[0]} -- key: {i[1]} -- values : {dic[i[1]]}")
    # print(i)

# get keys and values from dictionary
# print('@@@@@@@@@@@@@@@@@@@@')
# for i in dic.items():
#     print(f" key : {i[0]} -- value: {i[1]} ")

# print('@@@@@@@@@@@@@@@@@@@@@@@')
# for key, value in dic.items():
#     print(f" key: {key} -- value : {value}")


# get keys from dictionary
# for key in dic.keys():
#     print(key)

# get values from dictionary
# for value in dic.values():
#     print(value)

# break the loop on specific condition
for name in names:
    if 'Farhat' is name:
        print('found')
        break
    print(name)

# continue -- skip the current iteratrion on specific condition

for name in names:
    if name is 'Ali':
        continue
    print(f'Mail sended to {name}')


# for else
    
for name in names:
    if 'Farhat' is name:
        print('found')
        break
    print(name)
#  else case runs when loop successfully completed without break or any other intruption
else:
    print('For is completed')


# while loop
# example 1 
# count = 0
# while(count<=10):
#     print(count)
#     count += 1

# example 2
# count = 0
# check = True
# while(check):
#     print(count)
#     if count == 50:
#         check = False
#     count += 1