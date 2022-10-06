//exercice1

	//part 1
function infoAboutMe(){
	console.log("NIKIEMA Laurent 21 ans");
}

infoAboutMe();



	//part 2

function infoAboutPerson(personName, personAge, personFavoriteColor){
	console.log("your name is "+personName+",you are "+personAge+" year old "+" your favorite color is "+personFavoriteColor);

}

infoAboutPerson("David", 45, "blue");
infoAboutPerson("Josh", 12, "yellow");




//exercice2

function calculateTip() {
	let montantFacture=Number(prompt("montant de la facture"));
	if (montantFacture<50){
		let y=(20*montantFacture)/100;
	}
	else if ((montantFacture>=50)&&(montantFacture<=200)){
		let y=(15*montantFacture)/100;
	}
	else{
		let y=(10*montantFacture)/100;
	}

	console.log("the tip amount and the final bill "+(montantFacture+y));
};

calculateTip()



//exercice3

function isDivisible(){
	var j=0;
	for (var i =0; i <=500; i++) {
		if (i%23==0) {
			console.log(i)
			j=j+i;
		}
		
	}
	console.log("sum:"+j);
}


isDivisible();



//exercice4


var stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

var prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} 

var shoppingList=["banana", "orange", "apple"]; 

function myBill(){
	for (var i in shoppingList) {

		if (shoppingList[i] in stock) {
			console.log(shoppingList[i]);
		}
	}

myBill();