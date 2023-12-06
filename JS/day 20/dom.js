console.log('dom')

// get any elment in js using id
let heading = document.getElementById('heading')
// console.log(heading)

let paragraph = document.getElementById('paragraph')
// console.log(paragraph)

// get any element using class name

let anchorElement = document.getElementsByClassName('anchor')
console.log(anchorElement)
// get by using index
// console.log(anchorElement[0])

// get elements using loops
// console.log('using loop')
// for(let a of anchorElement ){
//     console.log(a)
// }

// get any element using tag name
// let element = document.getElementsByTagName('h1')
let element = document.getElementsByTagName('a')
// console.log(element)
// console.log(element[0])

// get any element using id or class or tag name

// let any_element = document.querySelector(' h1 ')
// let any_element = document.querySelector(' .anchor ')
let any_element = document.querySelector(' #heading ')
// console.log(any_element)

// get all element using id or class or tag name

// let all_elements = document.querySelectorAll('h1')
// let all_elements = document.querySelectorAll(' .anchor ')
let all_elements = document.querySelectorAll(' #heading ')
// console.log(all_elements)
// console.log(all_elements[0])


// get value/innerText content of any tag
let heading_element = document.getElementById('heading')
let heading_data = heading_element.innerText

// console.log(heading_element)
// console.log(heading_data)

let div_element_text = document.getElementById('container').innerText
let div_element_html = document.getElementById('container').innerHTML
console.log(div_element_text)
console.log(div_element_html)


