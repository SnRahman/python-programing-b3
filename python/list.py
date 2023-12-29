print('list')

# create a new list
li = [1,2,3,4,5,7,5]

# access list / element
print(li)
print(li[0])
print(li[5])

# update any index value
li[5] = 10
print(li)

# check type
print( type(li) )

# 2
print( isinstance(li,list) )
print( isinstance(li,str) )
print( isinstance(li,bool) )
print( isinstance(li,int) )
print( isinstance(li,float) )

# 3
if type(li) is list:
    print('list this is')
else:
    print('not a list')



# get length of a list

li_length = len(li)
print(li_length)

print( len(li))

# append new item record in list
li.append(1000)
# li.append( [45,25,36,78,91,0,47] )
print(li)


# append multiple items in list
li.extend( [45,25,36,78,91,0,47] )

print(li)

# append new items at given index
# li.insert(5,'string')
# li.insert(5,[1,45,24,5])
print(li)

# remove items from list by value
# li.remove(1000)
# li.remove(5)
print(li)

# remove last items form list
poped_item =  li.pop()

# remove value by index
poped_item =  li.pop(0)

print(li)
print(poped_item)

# get index of any value from list
# index = li.index(1000)
index = li.index(5)
print(index)

# count specific elements in list
count = li.count(5)
print(count)


# sort the list
# ascending order
# li.sort()

# descending order
# li.sort( reverse=True )

print(li)

# reverse the entire list items
li.reverse()
print(li)

# make list copy

li_copy = li.copy()
print(li_copy)

# clear the whole list
# li.clear()
print(li)


# in keyword to check weither item present in list or not
if 500 in li:
    print('present')
    index = li.index(500)
    print(index)  
else:
    print('not present') 


a = 20
b = '20'

# if a == b:
# type casting
if a is int(b):
    print('true')
else:
    print('false')



""" 
<li>Find the last element of an array without giving a hard-coded index.</li>
<li>Check whether the first or the last index of an array has a specified 
    value, let's say 5.</li>
<li>Make an array to store the names of students and check whether that
        array has your own name or not and also return the index of that value.</li>
<li>Add the array element at the specified index.</li>
<li>Delete the array element from the specified index.</li>
"""






