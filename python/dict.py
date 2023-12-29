print('dictionary')

arr = ['ahmad','ali','python',25,'ahmadali@gmail.com','030012345678']

# inilialize dictionary
dic = {
    'fname' : 'ahmad',
    'lname' : 'ali',
    'course' : 'python',
    'age' : 25,
    'email' : 'ahmadali@gmail.com',
    'phone' : '030012345678'
}

# access dictionary
print(dic)
print(dic['phone'])
print(dic['fname'])

# add new key in dictionary
# dic['address'] = 'lahore'
dic['pata'] = 'lahore'

# update any key in dictionary
dic['lname'] = 'Adeel'
print(dic)

# delete any key from dictionary
del dic['pata']
# del dic
print(dic)


# tuples

tup = (1,2,3,5,4,78,5,4,(1,2,5,4,7,8)) 

print(tup)
print(type(tup))
print(tup[2])
# tup[2] = 45
del tup[2]


