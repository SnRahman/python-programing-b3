// alert('external file')

let a = 0
let b = 2.5
let c = '0-9a-z-special characters'
let d = true 
let e = false
let f = [1,2.3,'string',true,['&','*',"+"]] 

let a1 =  [1]
// console.log(a1)
Name:
Email: 
Domain :
Invoice : 
// declare the array
let arr = [10,25,36,45,78,639] 

// console.log(arr)
// console.log(arr[0])
// console.log(arr[1])
// console.log(arr[2])
// console.log(arr[3])
// console.log(arr[4])
// console.log(arr[5])
// console.log(arr[6])

let arr1 = new Array()


// console.log(arr1)

// check data type of any variable
// 1
// console.log(typeof b)
// console.log(typeof a)
// console.log(typeof c)
// console.log(typeof d)
// console.log(typeof f)

//2 instanceof

// console.log( arr instanceof Array)
// console.log( a instanceof Array)

// 3 isinstance()
// console.log(Array.isArray(arr))
// console.log(Array.isArray(a))

// array functions

console.log(arr)

// toString function -  convert array to string

let arr_string = arr.toString()
console.log(arr_string)
// console.log( arr.toString() )


// join

// let arr_join = arr.join("+")
// let arr_join = arr.join(" ")
let arr_join = arr.join("")

console.log(arr_join)


// push - add new element in array at last

arr.push(700)
arr.push(700,800,900,80)
console.log(arr)

// pop - remove an element from last

arr.pop()
arr.pop()
console.log(arr)

// unshift() add new element in array at start

arr.unshift(1000)
arr.unshift(1000,2000,3000)
console.log(arr)

// shift remove an element form start

arr.shift()
arr.shift()
console.log(arr)

// splice function to add/ remove multiple values form array form specific index in between the start and end.
// splice(start_index,qty_to_be_removed)

arr.splice(2,4)
console.log(arr)

// add new elements in between the array
// arr.splice(4,0,9999,999,99,9)
arr.splice(4,2,9999,999,99,9)
console.log(arr)


// slice get chunk of array without affecting orignal array
let new_arr = arr.slice(2,8)

console.log(new_arr)

// delete any item from array

delete new_arr[2]

// new_arr[2] = 0

console.log(new_arr)

// string concatination
console.log( "10" + '2' )

console.log( new_arr + arr)

// concate function to merge two arrays

let arr2 = arr.concat(new_arr)
console.log(arr2)

// get index of any value from given array

let index = arr2.indexOf(99)

if(index == -1){
    console.log('value not found')
}else {
    console.log('Index is: '+ index)
}


// includes
console.log( arr2.includes(78) )
console.log( arr2.includes(585745) )


// console.log(index)





























