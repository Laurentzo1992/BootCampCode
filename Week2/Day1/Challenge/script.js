//Exercice 1

let fruits = ["Banana", "Apples", "Oranges", "Blueberries"];
//Suprimer Banana
fruits.splice(0,1);
//Trier par ordre alphabetique
fruits.sort()
//Ajouter Kiwi
fruits.push("Kiwi")
//Suprimer Aplles avec une methode differente de la premiere
fruits.shift()
//Trier par ordre inverse
fruits.reverse()










//Exercice 2

let moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
console.log(moreFruits[1][1])