function showReview(){
    document.querySelector(".review-con").style.opacity = "100%";
    document.querySelector(".product-img").style.filter = "brightness(0.4)"
}

function hideReview(){
    document.querySelector(".review-con").style.opacity = "0%";
    document.querySelector(".product-img").style.filter = "brightness(1)"
}

var sun = document.getElementById("sun-icon")
var moon = document.getElementById("moon-icon")
var body = document.getElementsByTagName("body")[0]
var introText = document.querySelector("#intro p")

function darkMode(){
    sun.style.display="none"
    moon.style.display="block"
    body.classList.toggle("body-dark")
    introText.style.color="#eeeff1"
}
function lightMode(){
    sun.style.display="block"
    moon.style.display="none"
    body.classList.toggle("body-dark")
    introText.style.color="#2f323a"
}