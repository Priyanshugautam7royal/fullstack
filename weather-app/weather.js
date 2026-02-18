const apikey = "ef5fa7c02115071accf6a67d4a2319df";
const apiurl = "https://api.openweathermap.org/data/2.5/weather?units=metric&q=";

const searchbox = document.querySelector(".search input");
const searchbtn = document.querySelector(".search button");
const weathericon = document.querySelector(".weather-icon");

async function checkWeather(city){
    const response = await fetch(`${apiurl}${city}&appid=${apikey}`);
    if(response.status == 404){
        document.querySelector(".error").style.display = "block"
        document.querySelector(".weather").style.display = "non"     
    }
    
    if(response.status == 404){
        alert("City not found");
        return;
    }

    const data = await response.json();
    

    document.querySelector(".city").innerHTML = data.name;
    document.querySelector(".temp").innerHTML = data.main.temp + "°C";
    document.querySelector(".humidity").innerHTML = data.main.humidity + "%";
    document.querySelector(".wind").innerHTML = data.wind.speed + " km/h";

    if(data.weather[0].main == "Clouds"){
        weathericon.src = "sun-cloud-removebg-preview.png";
    }
    else if(data.weather[0].main == "Clear"){
        weathericon.src = "WEATHER/sun-icon-removebg-preview.png";
    }
    else if(data.weather[0].main == "Rain"){
        weathericon.src = "WEATHER/rain-removebg-preview.png";
    }
    else if(data.weather[0].main == "Drizzle"){
        weathericon.src = "WEATHER/Drizzle.png";
    }
    else if(data,weather[0].main == "Mist"){
        weathericon.src = "WEATHER/Snow-removebg-preview.png"
    }
    document.querySelector(".weather").style.display = "block"
}

searchbtn.addEventListener("click", ()=>{
    checkWeather(searchbox.value);
});
