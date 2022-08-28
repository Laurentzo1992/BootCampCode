//Exercice 1


//Stockez votre nourriture préférée dans une variable
let nouriturePrefere = "Attienké";

//Enregistrez votre repas préféré de la journée dans une variable (c'est-à-dire petit-déjeuner, déjeuner ou dîner)
let repasPrefere = "Diner";

//Console.logI eat <favorite food> at every <favorite meal>
console.log("I eat"+" "+nouriturePrefere+" "+"at every"+" "+repasPrefere);

//Exercice 2

//Partie I


//En utilisant ce tableau :let myWatchedSeries = ["black mirror", "money heist", "the big bang theory"];


let myWatchedSeries = ["black mirror", "money heist", "the big bang theory"];


//Créez une variable myWatchedSeriesLengthdont le nom est égal au nombre de séries dans le myWatchedSeriestableau.

let myWatchedSeriesLength = myWatchedSeries.length


//Créez une variable nommée myWatchedSeriesSentence, qui est égale à une phrase décrivant la série que vous avez regardée

let myWatchedSeriesSentence = myWatchedSeries.join(",")


//Console.log une phrase utilisant les deux variables créées ci-dessus
//Par exemple :I watched 3 series : black mirror, money heist, and the big bang theory

console.log("I watched"+" "+myWatchedSeriesLength+" "+"series"+" "+myWatchedSeriesSentence)

//Partie II

//variable contenant mes series
let myWatchedSeries = ["black mirror", "money heist", "the big bang theory"];
//voir combien j'ai de serie
let myWatchedSeriesLength = myWatchedSeries.length
//joindre les element de mon tableau

let myWatchedSeriesSentence = myWatchedSeries.join(",")
//lire mes variable

console.log("I watched"+" "+myWatchedSeriesLength+" "+"series"+" "+myWatchedSeriesSentence);
//suprimer "the big bang theory" et remplacer par friends

myWatchedSeries.splice(2,1,"friends");

//ajouter une serie de mon choix à la friends
myWatchedSeries.push("24 heure chrono")

//Ajoutez, au début du tableau, le nom de votre série préférée.

myWatchedSeries.splice(0,0,"arow");

//Supprimer la série « miroir noir »
myWatchedSeries.splice(1,1,);

//Console.log la troisième lettre de la série "money heist".
 console.log(myWatchedSeries[1][2])

//Enfin, console.log le myWatchedSeriestableau, pour voir toutes les modifications que

console.log(myWatchedSeries);


//Exercicie 3

//var temperature en celsus
let temperateureCelsus = 50;
//var temperature en fahrenheit
let temperateureFahrenheit = ((temperateureCelsus*9)/5)+32;
//affichage de la temperature en Fahrenheit
console.log(temperateureFahrenheit);

//Exercice 4

//1
let c;
    let a = 34;
    let b = 21;

    console.log(a+b)
// Prediction: It will output 55, because 34 and 31 are numbers
//Actual 55

//2
 a = 2;
 console.log(a+b)
// Prediction: It will output 23, because 34 and 31 are numbers
//Actual 23

//3

// Prediction: undefined
//Actual undefined

//4
// Prediction: 75
//Actual 75




//Exercice 5


typeof(15)
// Prediction: number
// Actual: number

typeof(5.5)
// Prediction: float
// Actual: number

typeof(NaN)
// Prediction: number
// Actual: number

typeof("hello")
// Prediction: string
// Actual: typeof("hello")

typeof(true)
// Prediction: boolean
// Actual: boolean

typeof(1 != 2)
// Prediction: boolean
// Actual: boolean

"hamburger" + "s"
// Prediction: hamburgers
// Actual: hamburgers

"hamburgers" - "s"
// Prediction:
// Actual: NaN

"1" + "3"
// Prediction: 13
// Actual: 13

"1" - "3"
// Prediction:
// Actual: -2

"johnny" + 5
// Prediction: johnny5
// Actual: johnny5

"johnny" - 5
// Prediction: NaN
// Actual: NaN

99 * "hello" 
// Prediction: NaN
// Actual: NaN

1 != 1
// Prediction: false
// Actual: false

1 == "1"
// Prediction: true
// Actual: true

1 === "1"
// Prediction: false
// Actual: false


//Exercice 6



5 + "34"
// Prediction: 534
// Actual: 534

5 - "4"
// Prediction: 1
// Actual: 1

10 % 5
// Prediction: 0
// Actual: 0

5 % 10
// Prediction: 5
// Actual: 5

"Java" + "Script"
// Prediction:JavaScript
// Actual: JavaScript

" " + " "
// Prediction: 
// Actual:

" " + 0
// Prediction: 0
// Actual: 0

true + true
// Prediction:
// Actual: 2

true + false
// Prediction: 1
// Actual: 1

false + true 
// Prediction: 1
// Actual: 1

false - true
// Prediction: -1
// Actual: -1

!true
// Prediction:
// Actual: false

3 - 4
// Prediction: -1
// Actual: -1

"Bob" - "bill"
// Prediction: NaN
// Actual: NaN