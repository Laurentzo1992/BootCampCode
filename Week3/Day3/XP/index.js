//Exercice 1


//  let my_h1 = document.getElementsByTagName("h1");
//  alert("Content in the h1 is " + my_h1[0].innerHTML);

// let my_article = document.getElementsByTagName("article")[0].lastChild;
// my_article.removeChild(my_article.lastElementChild);

// document.addEventListener('click', function(){
// 	let h3Element = document.getElementsByTagName("h3")[0];
// 	h3Element.style.display = "none";
// })


// let btn = document.createElement("input");
// btn.setAttribute("type", "button");
// btn.appendChild("body");
// document.addEventListener('click', function(){
// 	btn.style.font-weight = "bold";
// });


//Exercice 2

// let input1 = document.getElementById("fname").value
// let input2 = document.getElementById("lname").value
// let input3 = document.getAttribute('fname').value
// let input4 = document.getAttribute('fname').value

// console.log(input1, input2)
// console.log(input3, input4)


var myForm = document.getElementsByTagName('form')[0];
myForm.addEventListener('submit', function(e) {
alert('Vous avez envoyé le formulaire !');
e.preventDefault();
let input1 = document.getElementById("fname").value;
let input2 = document.getElementById("lname").value;
li1 = document.createElement("li");
li2 = document.createElement("li");
ulEl = document.getElementsByClassName("usersAnswer");
li1.appendChild(ulEl);
li2.appendChild(ulEl);
li1.innerHTML = input1;
li2.innerHTML = input2;
}, true);
