
function LongueurEtoile(mots) {
	let etoileTaille = 0;
	for (let x of mots)
		if (etoileTaille < x.length) 
			etoileTaille = x.length;
	return etoileTaille;
}

function AfficheEtoile(etoileTaille) {
	let etoile = "*";
	for (var i = etoileTaille + 4; i > 1; i--) 
		etoile = etoile + "*";
	return etoile;
}

function afficheMot(mots) {
	mots = mots.split(",");
	etoileTaille=plusGrand(mots);
	etoile=etoile(etoileTaille);
	console.log(etoile);
	for (let x of mots) {
		let mot = "* " + x;
		for (i=mot.length; i < etoileTaille+3; i++)
			mot = mot + " ";
		console.log(mot + "*");
	}
	console.log(etoile);
}

afficheMot(prompt("Entrez plusieurs mots séparés par des virgules"));