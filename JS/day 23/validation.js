let form = document.getElementById('form')
form.addEventListener('submit',(e)=>{
    e.preventDefault()
    console.log('form is submitted')

    // first name validations
    let f_name = document.getElementById('f_name').value
    let f_name_error = document.getElementById('f_name_error') 
    
    if(f_name == '' ){
    //    let f_name_error = document.getElementById('f_name_error') 
    //    f_name_error.innerText = '*first name is required'
        f_name_error.innerText = '*first name is required'
    } else {
        f_name_error.innerText = ''
    }

    // Last name validations
    let l_name = document.getElementById('l_name').value
    let l_name_error = document.getElementById('l_name_error')

    if(l_name == ''){
        l_name_error.innerText = '*Last name is required'
    } else {
        l_name_error.innerText = ''
    }

    // email validations
    let email = document.getElementById('email').value
    let email_error = document.getElementById('email_error')
    // console.log(email.includes('@'))
    if ( !email.includes('@') ||  !email.includes('.') ){
        email_error.innerText = '*Enter a Valid email'
    } else {
        email_error.innerText = ''
    }

    // phone number validation
    let phone = document.getElementById('phone').value
    let phone_error = document.getElementById('phone_error')
    console.log(phone.length)

    if (phone == ''){
        phone_error.innerText = '*Phone Number is required'
    }else if( phone.length != 11 ){
        phone_error.innerText = '*Phone Number Should be of 11 digits'
    } else {
        phone_error.innerText = ''
    }

    // age validations
    let age = document.getElementById('age').value
    let age_error = document.getElementById('age_error')

    // age>=18 && age<=65
     if( age<18 || age>65){
        age_error.innerText = '*Age should be between 18 - 65'
    }else{
        age_error.innerText = ''
    }

    // password validations
    let password = document.getElementById('password').value
    let password_error = document.getElementById('password_error')

    if(password.length< 8 || password.length > 20  ){
        password_error.innerText = 'Password should be betwen 8 - 20 characters'
    }else {
        password_error.innerText = ''
    }


    // confirm password

    let confirm_password = document.getElementById('confirm_password').value
    let confirm_password_error = document.getElementById('confirm_password_error')

    if(confirm_password =='' && password =='' ){
        confirm_password_error.innerText = 'password is required'
    } else if(  password != confirm_password){
        // confirm_password_error.innerText = " Password Does't match"
        confirm_password_error.innerText = ' Password Does\'t match'
    } else {
        confirm_password_error.innerText = ''
    }

    console.log(f_name)

   
    

})


// task related
let fresher = document.getElementById('fresher')
let experience = document.getElementById('experience') 

let edu_details_div = document.getElementById('edu_details_div')
let exp_details_div = document.getElementById('exp_details_div')
 fresher.addEventListener('click', function(){
    //  console.log('fresher')
    edu_details_div.style.display = 'block'
    exp_details_div.style.display = 'none'
 });

 experience.addEventListener('click',function(){
    exp_details_div.style.display = 'block'
    edu_details_div.style.display = 'none'

 })