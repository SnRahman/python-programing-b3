let btn = document.getElementById('btn')

// method 1 using general function
btn.addEventListener('click',click)
let div = document.getElementById('div')
function click(){
    btn.style.backgroundColor = 'red'
    btn.style.color = 'white'
    btn.style.border = 'none'
    btn.innerText = 'clicked'
    div.style.display = 'none'
}

// method 2 using anonymeous function
let arrow = document.getElementById('arrow')
// arrow.addEventListener('click', function () {} )
arrow.addEventListener('click',() => {
    alert('Clicked using arrow function')
})

// on mouse over event
let mouse_over = document.getElementById('mouse_over')
mouse_over.addEventListener('mouseover',function () {
    console.log('mouse over triggered')
    mouse_over.style.backgroundColor = 'yellow'
})

mouse_over.addEventListener('mouseout',function(){
    console.log('mouse out triggered')
    mouse_over.style.backgroundColor = '#E5E5E5'
})

// on mouse out event
let mouse_out = document.getElementById('mouse_out')
mouse_out.addEventListener('mouseout',() => {
    console.log('mouse out triggered')
})

// on focus event on input

let name = document.getElementById('name')
name.addEventListener('focus',() => {
    console.log('User is entering name')
})

// on blur event on input

let password = document.getElementById('password')
password.addEventListener('blur',() => {
    console.log('User is gone')
    password.style.border = '3px solid red'

})


let form = document.getElementById('form')
form.addEventListener('submit',function(a){
    a.preventDefault()

    console.log('form is submitted.')
})

// execute an event once
let once = document.getElementById('once')
once.addEventListener('click',once_function)

function once_function(){
    console.log('event is triggered.')

    once.removeEventListener('click',once_function)
}

// 
let outer = document.getElementById('outer')
let inner = document.getElementById('inner')



outer.addEventListener('click',(e)=>{
    // e.stopPropagation()
    console.log('outer is clicked (capturing)')
},true)


inner.addEventListener('click',(e)=>{
    // e.stopPropagation()
    console.log('inner is clicked (capturing)')
},true)


let btn1 = document.getElementById('btn1')
btn1.addEventListener('click',(e)=>{
    // e.stopPropagation()
    console.log('btn is clicked')
})

inner.addEventListener('click',()=>{
    console.log('inner is clicked')
})


outer.addEventListener('click',(e)=>{
    // e.stopPropagation()
    console.log('outer is clicked')
})


// tasks related
let fun_facts = [
    'The oldest person ever to have lived (whose age could be authenticated), a French woman named Jeanne Louise Calment, was 122 years old when she died in 1997.',
    'The oldest person ever to have lived (whose age could be authenticated), a French woman named Jeanne Louise Calment, was 122 years old when she died in 1997.',
    'The oldest person ever to have lived (whose age could be authenticated), a French woman named Jeanne Louise Calment, was 122 years old when she died in 1997.',
    'The oldest person ever to have lived (whose age could be authenticated), a French woman named Jeanne Louise Calment, was 122 years old when she died in 1997.',
    'The oldest person ever to have lived (whose age could be authenticated), a French woman named Jeanne Louise Calment, was 122 years old when she died in 1997.',
    'The oldest person ever to have lived (whose age could be authenticated), a French woman named Jeanne Louise Calment, was 122 years old when she died in 1997.',
]

// console.log( Math.floor(Math.random() * fun_facts.length ))
// console.log( Math.floor(Math.random() * 6 ))


























console.log(btn)