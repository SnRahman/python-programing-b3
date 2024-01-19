// make array of questions
let questions = [
    {
        'title' : 'What is 10 / 2?',
        'options' : [14,25,5,78],
        'answer' : 5
    },
    {
        'title' : 'What is 15 - 10?',
        'options' : [10,5,36,12],
        'answer' : 5
    },
    {
        'title' : 'What is 4 + 10?',
        'options' : [10,14,36,12],
        'answer' : 14
    },
    {
        'title' : 'What is the capital of Pakistan?',
        'options' : ['Lahore','Islamabad','Faisalabad','Multan'],
        'answer' : 'Islamabad'
    },
] 

// initialise variables
let question_index = 0
let result = 0

// console.log(questions[question_index])
let container = document.getElementById('quiz_container')

// function to start the game on start button click
function start(){
    question_index = 0
    result = 0

    let start_btn = document.getElementById('start')
    start_btn.addEventListener('click',function(){
        add_question()
    })
}

// call the start function
start()

// function for displaying new question on the screen every time
function add_question(){
    let current_question = questions[question_index]

    // make html for question or add new question
    container.innerHTML = '<h1>'+ current_question.title +'</h1>' 
    for(let option of current_question.options){
        
        let option_btn = document.createElement('button')
        option_btn.innerText = option
        option_btn.classList.add('option-btn')
        container.append(option_btn)
    }
    check_answer()

}

// function for evaluating the user option seletion and then displaying the next question
function check_answer(){
    // add events on options
    let options = document.querySelectorAll('button')
    let current_question = questions[question_index]

    for(let option of options){
        option.addEventListener('click',function(){
            // console.log(option.innerText)

            // check if user selection is matched with the correct answer
            if( this.innerText == current_question.answer  ){
                result++
            }

            question_index++

            //place check weither diplay new question of end the game if question finished.
            if(question_index < questions.length ){
                add_question()
            }else{
                game_over()
            }
            // console.log(this.innerText)
        })
    }
}

// function of creating end game elements
function game_over(){
    container.innerHTML = '<h1>Game Over!</h1> <br> <h1> Score: ' + result +'/'+ questions.length + '</h1><form><input type="hidden" value="'+ result + '"><button id="start">Restart</button> </form> '

    // let restart_button = document.createElement('button')
    // restart_button.setAttribute('id','start')
    // restart_button.innerText= "Restart"
    // container.append(restart_button)
    // container.append('</form>')
    // container.innerHTML += '<button id="start">Restart</button> </form>'
    start()
}