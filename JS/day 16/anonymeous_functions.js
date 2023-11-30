// general function


function display(){
    console.log('hello World!')
}

function add(a,b){
    // let result = a+b
    console.log(a+b)
}

// returning functions
function mul(a,b){
    let result = a*b
    // console.log(result)
    return result
}

let result = mul(12,2)
console.log('result :' + result)

// add(1,5)

// display()

// anonymeous functions
// without parameters
let display1 = function (){
    console.log('hello World! anony')
}

// display1()

// with parameters
let add1 = function (a,b){
    console.log(a+b)
}

// add1(5,10)
// add1(15,10)
// add1(5,25)
// add1(78,22)

// console.log( typeof display1)
// console.log( typeof add1)

// returning functions

let mul1 = function (c,d){
    return c*d
}

let result1 = mul1(14,5)
console.log('result1 :' + result1)
// console.log('direct result :' + mul1(14,5))


// Arrow functions
// let display2 = function () {}

let display2 = () => {
    console.log('Hello World! Arrow')
}

display2()


let add2 = (a,b) => { console.log(a+b) }
add2(50,56)

// returing function

// let mul2 = (c,d) => { return c*d}
let mul2 = (c,d) => c*d

let result2 =  mul2(15,5)

console.log(result2)

// examples
// find square of given number

// 1 general function
function square(number){
    return number**2
}

let square_result = square(5)
console.log(square_result)

// 2- anonymeous function

let square1 = function (number) {
    return number**2
}

let square_result1 = square1(10)
console.log(square_result1)

// 3- arrow function

let square2 = (number) => number**2  

let square_result2 = square2(15)
console.log(square_result2)


// single line if else
let number = 5
function check_number(number){
    if(number%2 == 0){ console.log('even')} else { console.log('odd') }
}


// check_number(25)

let check_number2 = (number) =>  number%2==0 ? console.log('even') : console.log('odd')
check_number2(30)


let check_number3 = (number) =>  number%2==0 ? 'even' : 'odd'
let ouptut = check_number3(30)
console.log(ouptut)
// number%2==0 ?console.log('even') :console.log('odd')


// function as a parameter
function sum(a,b){
    console.log(a+b) 
}

function general(a,b,logic){
    console.log( logic(a,b) )
}



general(2,10, function (a,b) { return  a+b})
general(2,10, (a,b) => { return  a-b})
general(2,10, (a,b) => { return  a*b})
general(2,10, (a,b) => { return  a/b})
general(2,10, (a,b) => { return  a%b})
general(2,10, (a,b) => { return  a**b})








function div(a,b){
    console.log(a-b) 
}

// check length of any string
let string = ' hello '
console.log(string.length)






// sum(4,6)

