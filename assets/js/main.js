/* =========================
   Mobile Menu Toggle
========================= */

document.addEventListener("DOMContentLoaded", function () {

const menuButton = document.querySelector(".menu-toggle");
const nav = document.querySelector(".main-nav");

if(menuButton){
menuButton.addEventListener("click", function(){
nav.classList.toggle("active");
});
}

/* =========================
   Live Search Filter
========================= */

const searchInput = document.getElementById("search");

if(searchInput){

searchInput.addEventListener("keyup", function(){

let filter = searchInput.value.toLowerCase();

let cards = document.querySelectorAll(".card");

cards.forEach(function(card){

let text = card.innerText.toLowerCase();

if(text.includes(filter)){
card.style.display = "block";
}else{
card.style.display = "none";
}

});

});

}

/* =========================
   Scroll To Top Button
========================= */

const topButton = document.createElement("button");

topButton.innerText = "↑";

topButton.id = "scrollTop";

document.body.appendChild(topButton);

window.addEventListener("scroll", function(){

if(window.scrollY > 400){

topButton.style.display = "block";

}else{

topButton.style.display = "none";

}

});

topButton.addEventListener("click", function(){

window.scrollTo({
top:0,
behavior:"smooth"
});

});

/* =========================
   Smooth Anchor Scroll
========================= */

document.querySelectorAll('a[href^="#"]').forEach(anchor => {

anchor.addEventListener("click", function(e){

e.preventDefault();

document.querySelector(this.getAttribute("href")).scrollIntoView({

behavior:"smooth"

});

});

});

});
