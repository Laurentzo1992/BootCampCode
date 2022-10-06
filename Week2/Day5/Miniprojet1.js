//Exercice 1 : Jeu devinette

	function checkNumber(nombre) {
		type = Number(nombre);
		if (!type) {
			console.log("Value most be a number");
			return false;
		} else if (nombre < 0 && nombre > 10){
			console.log("number is not valide");
			return false;
		} else {
			return true;
		}
	}

	function randomNumber(min,max) {
		min = Math.ceil(min);
		max = Math.floor(max+1);
		let nombre = Math.floor(Math.random()* (max - min)) + min;
		return nombre;
	}

	function playTheGame() {
		let confirmation=confirm("Voulez vous jouer au jeu?")
		if (!confirmation) {//1
			console.log("Bye Bye!!");
			return;
		} else {//2
			let userNumber;
			do {
				userNumber = prompt("Entrez un nombre entre 0 et 10 : ");
				if (checkNumber(userNumber)) {
					computerNumber = randomNumber(0,10);
					NumberChoice(userNumber,computerNumber);
				}
			} while (!checkNumber(userNumber))//prime
		}

	}

	//Deuxieme partie
	function NumberChoice(inpuNumber,randomNumber) {
		let i=0;
		while(i!=4) {
			if (inpuNumber == randomNumber) {
				alert("WINNER");
				return;
			} else if (inpuNumber > randomNumber && i!=3) {
				inpuNumber = prompt("numéro plus grand que le numero choisir au hasard, ressayé à nouveau"); 
				while(!checkNumber(inpuNumber))
					inpuNumber = prompt("Entrez un nombre entre 0 et 10");
			}
			else if (inpuNumber < randomNumber && i!=3) {
				inpuNumber = prompt("numéro plus grand que le numero choisir au hasard, ressayé à nouveau"); 
				while(!checkNumber(inpuNumber))
					inpuNumber = prompt("Entrez un nombre entre 0 et 10");
			}	
			else if ( i == 3) {
				alert("perdu!!");
				return;
			}
			i++;
		}
	}