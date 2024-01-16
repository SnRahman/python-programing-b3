
let previous_todo_lists = localStorage.getItem('todo_items')
document.getElementById('items_container').innerHTML = previous_todo_lists

add_item_events()


let form = document.getElementById('form')
form.addEventListener('submit',function(e){
    e.preventDefault()

    add_new_item()
    save_todo()
    add_item_events()
})


function save_todo(){
     // save data in browser local storage
     let current_todo_lists = document.getElementById('items_container').innerHTML
     // console.log(current_todo_lists)
     localStorage.setItem('todo_items',current_todo_lists)
}

function add_new_item(){
    let todo = document.getElementById('todo_input').value
    
    let li = document.createElement('li')
    li.classList.add('li-item')
    // li.innerHTML = '<span>'+ todo +'</span> <button id="item-btn">X</button>'

    let li_content = '<span>'+ todo +'</span> <button id="item-btn">X</button>'
    li.innerHTML = li_content
    
    let items_container = document.getElementById('items_container')
    items_container.prepend(li)
    
    document.getElementById('todo_input').value = ''
}

function add_item_events(){
    let lis = document.querySelectorAll('.li-item')
    for(let li of lis){
        let span = li.children[0]
        
        span.addEventListener('click',function(){
            this.classList.add('mark')
            save_todo()
            // this.style.color = 'red'
            // this.style.backgroundColor = 'Yellow'
            // this.style.textDecoration = 'line-through'
        })

        // let delete_button = li.children[1]
        li.children[1].addEventListener('click',function(){
            li.remove()
            save_todo()
        })
        
    }
}