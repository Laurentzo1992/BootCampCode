//Exercice 1


let langue = prompt("Quelle est votre langues ?");
langueChoisie = langue.toLowerCase();
if (langueChoisie=="francais"){
    alert("Bonjour !");
}
else if(langueChoisie=="anglais"){
    alert("Hello !");
}
else if(langueChoisie=="hebreu"){
    alert("Shalom !");
}
else{
    alert("01110011 01101111 01110010 01110010 01111001");
}

//Exercice 2

let userNote = prompt("Quelle votre note: ?");
userNote = parseInt(userNote);

if(userNote>90){
    console.log("A")
}
else if(userNote>80 && userNote<=90){
    console.log("B")
}
else if(userNote>=70 && userNote>=80){
    console.log("C")
}
else {
    console.log("D")
}

//Exercice 3

let chaine = prompt("Saisir une chaine: ?");

if(chaine.length>=3 && chaine.length)