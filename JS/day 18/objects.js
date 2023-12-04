let arr = [1,23,45,6,78,75]
let arr1 = [1,230.32,'45',true,78,75]

console.log(arr1)

// multi dimentional array

let arr2 = [ 
    [ 1,2,3,45,6],
    [123,45,78,99],
    ['a','b','c']
]
console.log(arr2)
console.log(arr2[0][2])
console.log(arr2[1][0])
console.log(arr2[2][1])

// 3 dimentional array
let arr3 = [ [ [1,2,5,4] ] ]

console.log(arr3)
console.log(arr3[0])
console.log(arr3[0][0])
console.log(arr3[0][0][3])


// object

let student = ['ahmad','mubeen','python','18','ahmadmubeen@gmail.com','030012345678']

let student_obj = {
    first_name : 'ahmad',
    last_name : 'mubeen',
    course : 'python',
    age : 18,
    email : 'ahmadmubeen@gmail.com',
    phone : '030012345678'
}

console.log(student)
console.log(student_obj)
// acces objects value
// method 1
console.log(student_obj['first_name'])
console.log( student_obj['last_name'] )
console.log( student_obj['course'] )

// method 2
console.log( student_obj.age)
console.log( student_obj.email)
console.log( student_obj.phone)

// add new key in object
student_obj['address'] = 'lahore'
console.log(student_obj.address)
console.log(student_obj['address'])
student_obj.address1 = 'karachi'
console.log(student_obj)

// update existing key
student_obj.last_name = 'usman'
student_obj['course'] = 'Web Development'
console.log(student_obj)

// delete object key

delete student_obj.address1
delete student_obj['last_name']
console.log(student_obj)

// reset any key value

student_obj.age = -1
student_obj['email'] = ''
console.log(student_obj)


// get keys of any object
let student_keys = Object.keys( student_obj )
console.log(student_keys)


// get values of nay object```

let student_values = Object.values( student_obj )
console.log(student_values)


// get both keys and values in arrays

let keys_values = Object.entries( student_obj )
console.log(keys_values)
console.log(  keys_values[4] )
console.log(  keys_values[4][0] )
console.log(  keys_values[4][1] )




