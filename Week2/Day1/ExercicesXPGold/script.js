//Exercice 1

let sentence = ["my","favorite","color","is","blue"];
//Écrivez un code Javascript simple qui rejoindra tous les éléments du tableau ci-dessus, et console.log le résultat.
sentence.join(",");

//Exercice 2

let str1 = "mix";
let str2 = "pod";

//Découpez et échangez les 2 premiers caractères des deux chaînes de la partie 1.

str3 = str1.slice(0,2)+str2.slice(2,3);
str3 = str2.slice(0,2)+str1.slice(2,3);


//Exercice 3


let num1 = parseInt(prompt("Saisir le nombre 2"));
let num2 = parseInt(prompt("Saisir le nombre 2"));
alert("la somme est : " +`${num2}`+`${num2}`)