let form = document.getElementById('form')
const api_key = '3d94d884787c276b1107b5e5cac522ab'
const kelvin_unit = 272.15
const lat = 31.582045
const lon = 74.329376
let days = 7
form.addEventListener('submit',async function(e){
    e.preventDefault()
    
    let city_name = document.getElementById('city_name').value

    if(city_name == ''){
        alert('Enter a valid city')
    }else {
        // let api_url = "https://api.openweathermap.org/data/2.5/weather?q="+city_name+ "&appid="+api_key
        let api_url = `https://api.openweathermap.org/data/2.5/weather?q=${city_name}&appid=${api_key}`
        
        // daily forcast data
        // let api_url = `https://api.openweathermap.org/data/2.5/forecast/daily?q=${city_name}&cnt=${days}&appid=${api_key}`
        // let api_url = `https://api.openweathermap.org/data/2.5/forecast?q=${city_name}&appid=${api_key}`

        // air populaiton api
        // let api_url = `http://api.openweathermap.org/data/2.5/air_pollution?lat=${lat}&lon=${lon}&appid=${api_key}`
        let response = await fetch(api_url)
        let data = await response.json()

        get_date(data)
        get_location(data)
        get_temp(data)
        get_weather(data)
        get_humidity(data)
        get_pressure(data)
        console.log(data)
        console.log(response)
        console.log(api_url)

    }
})

function get_date(data){
    let dt = data.dt * 1000
    let short_months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
    let date_obj = new Date(dt)
    let month_index = date_obj.getMonth()
    let month = short_months[month_index]
    let date = date_obj.getDate()
    let hours = date_obj.getHours()
    let minutes = date_obj.getMinutes()

    let ampm = ''
    if(hours >12){
        ampm = 'PM'
        // hours -= 12
        hours = hours - 12
    }else {
        ampm = 'AM'
    }

    let finel_date = `${month} ${date}, ${hours}:${minutes}${ampm} `
    document.getElementById('date').innerText = finel_date
}

function get_location(data){
    let city = data.name
    let country = data.sys.country
    let location = `${city}, ${country} `
    document.getElementById('location').innerText = location
}

function get_temp(data){
    let temp = (data.main.temp - kelvin_unit).toFixed(0) 
    let finel_temp = ` ${temp}&deg; C`
    document.getElementById('temp').innerHTML = finel_temp
}

function get_weather(data){
    let feels_like = (data.main.feels_like - kelvin_unit).toFixed(0)
    let weather_condition = data.weather[0].main
    let finel_feels_like = `${feels_like}&deg; C ${weather_condition}  `        
    document.getElementById('feels_like').innerHTML = finel_feels_like
}

function get_humidity(data){
    let humidity = data.main.humidity
    document.getElementById('humidity').innerText = humidity
}

function get_pressure(data){
    let pressure = data.main.pressure
    document.getElementById('pressure').innerText = pressure
}