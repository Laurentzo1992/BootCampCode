//Exercicie 1

//Parcourez le tableau ci-dessus et déterminez si chaque nombre est divisible par trois ou non.
Chaque fois que vous bouclez console.log trueou false.
let numbers = [123, 8409, 100053, 333333333, 7]
for (let i=0; i<numbers.length; i++){
    if(numbers[i]%3==0){
        console.log(true);
    }
    else{
        console.log(false);
    }
}

//Exercicie 2

let guestList = {
  randy: "Germany",
  karla: "France",
  wendy: "Japan",
  norman: "England",
  sam: "Argentina"
}









//Exercicie 3

//Tableau d'élément
let age = [20,5,12,43,98,55];
//Déclaration et initialise la variable $somme
let somme = 0;
//Déclaration et initialise le Maximun du tableau
let max = 0;
//Boucle sur l'ensemble des éléménets du tableau
for (let i=0; i<age.length; i++){
	//pour élémént ajouter en sommant la varaible $somme
    somme = somme+age[i];
    //si l'element est superieur a max max = l'element 
    if (age[i]>max){
        max = age[i];
    }
}

//affiche somme et max
console.log(somme);
console.log(max);