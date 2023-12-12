// create a button that changes its background color when clicked.

let change_bg = document.getElementById('change_bg')

change_bg.addEventListener('click',() => {
    console.log('clicked')
    let color = 'green'
    current_bg = change_bg.style.backgroundColor

    if(current_bg == color){
        change_bg.style.backgroundColor = 'white'
    } else {
        change_bg.style.backgroundColor = color
    }
})


// 2 - build a counter that increments when a button is clicked and displays the count on the page.

let inc_btn = document.getElementById('inc_btn')

inc_btn.addEventListener('click', function(){
    console.log('clicked')

    let qty_element = document.getElementById('qty')
    let qty = qty_element.value
    qty++
    // qty_element.innerText = qty
    qty_element.setAttribute('value',qty)
    console.log(qty)
})


// 3- create a list of items. implement a way to remove an item when it is clicked.
// let items = document.querySelectorAll('.item')
let items = document.getElementsByClassName('item')
console.log(items)

for(let item of items ){
    item.addEventListener('click',function(){
        item.remove()
        // this.remove()
    })
}
// console.log(items[0])



// 4 - create a button that enlarges the image when clicked.
let img_enlarge = document.getElementById('img-enlarge')

img_enlarge.addEventListener('click',()=>{
    // let img = document.getElementById('img');
    // img.style.width = '500px'

    document.getElementById('img').style.width = '500px'
})


// 5- create a color picker that changes the background color of a page element based on user selections.
let color_picker_btn = document.getElementById('color-picker')
color_picker_btn.addEventListener('click',function(){
    let color = document.getElementById('color').value
    document.querySelector('body').style.backgroundColor = color
})

// 6- implement a form that dynamically adds new input fields when a button is clicked.
let add_input = document.getElementById('add-input')
let count = 2
add_input.addEventListener('click',function(){
    let new_input = document.createElement('input')
    new_input.setAttribute('type','text')
    new_input.setAttribute('placeholder','input-' + count)
    new_input.setAttribute('name','input-' + count)
    
    document.getElementById('inputs').append(new_input)
    count++
    console.log(new_input)
})


// 7 - create a function that displays an alert with a random fun fact when clicked.
let fun_facts = [
    'Canada is south of Detroit (just look at a map).',
    'Bats are the only mammal that can actually fly.',
    'Elephants can’t jump',
    'Cows don’t actually have four stomachs; they have one stomach with four compartments.',
    'The platypus doesn\'t have a stomach at all: Their esophagus goes straight to their intestines',
    'Tigers’ skin is actually striped, just like their fur. Also, no two fur patterns are alike.'
]

let fun_fact_btn = document.getElementById('fun-fact')

fun_fact_btn.addEventListener('click', function(){
    let index = Math.floor(Math.random() * fun_facts.length)

    document.getElementById('fun-fact-item').innerText = fun_facts[index]
})


