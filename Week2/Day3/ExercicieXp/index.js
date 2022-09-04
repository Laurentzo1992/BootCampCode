
//Exercicie 1

let people = ["Greg", "Mary", "Devon", "James"];

//Écrivez du code pour supprimer "Greg" du peopletableau.
people[0].pop()

//Écrivez le code pour remplacer "James" par "Jason".


//Écrivez du code pour ajouter votre nom à la fin du peopletableau.


//Écrivez le code qui donne l'index de "Foo". Pourquoi renvoie-t-il -1 ?



//Créez une variable appelée last dont la valeur est le dernier élément du tableau.
//Astuce : Quelle est la relation entre l'indice du dernier élément du tableau et la longueur du tableau ?

let last = people.at(-1);


// Exercice 3

let numberForUser = Number(prompt("Give one number : "));
while(numberForUser <10 ){
    let numberForUser = Number(prompt("Give one number : "));
     alert(typeof(numberForUser));
}



//Exercice 4


let building = {
    numberOfFloors : 4,
    numberOfAptByFloor : {
        firstFloor : 3,
        secondFloor : 4,
        thirdFloor : 9,
        fourthFloor : 2,
    },
    nameOfTenants : ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan :  [4, 1000],
        david : [1, 500],
    },
}

//Console.log le nombre d'étages du bâtiment.
console.log(building.numberOfFloors);

//Console.log combien d'appartements sont aux étages 1 et 3.
console.log(building.numberOfAptByFloor.firstFloor +" et "+ building.numberOfAptByFloor.thirdFloor);

//Console.log le nom du deuxième locataire et le nombre de pièces qu'il possède dans son appartement.
console.log(building.nameOfTenants[1]);

//Vérifiez si la somme du loyer de Sarah et de David est supérieure au loyer de Dan. Si c'est le cas, augmentez le loyer de Dan à 1200.





//Exercicie 7

let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];

//Un groupe d'amis a décidé de créer une société secrète. Le nom de la société
// sera la première lettre de chacun de leurs noms triés par ordre alphabétique.
let nom = [];
for (let i of names){
  let code = names[i][0];
  nom.push[code];
}

console.log(sort(nom));
////////////////////////////////////////////////////////////////////////////////////////////////////
