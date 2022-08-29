//Exercice 1

let x = 50;
let y = 20;
if (x < y){
    console.log("x is the biggest number");
} 
else {
    console.log("y is the biggest number");
}


//Exercice 2

let newDog = "Chihuahua";
console.log(newDog.length);
console.log(newDog.toUpperCase());
console.log(newDog.toLowerCase());
if (newDog===`Chihuahua`){
    console.log("J'adore les chihuahuas, c'est ma race de chien préférée")
}
else {
    console.log("Je m'en fous, je préfère les chats")
}

//Exercice 3

let nombre = Number(prompt("ENTREZ UN NOMBRE : "));

if (nombre%2===0){
    alert("x est un nombre pair");
    }
else {
    (" x est un nombre impair");
}

//Exercice 4

let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];
if(users.length==0){
    console.log("personne n'est en ligne");
}
else if (users.length==1){
    console.log(users[0], "est en ligne");
}
else if(users.length==2){
    console.log(users[0], "et", users[1], "sont en ligne");
}
else{
    console.log(users[0], users[1], "et", users.length-2, "de plus sont en ligne");
}