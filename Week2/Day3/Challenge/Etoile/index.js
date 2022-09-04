
let etoile = "*";
for (let i=0; i < 8; i++)
{
  console.log(etoile);
    etoile += "*";
}

////////////////////////////////////////////
let etoile = "*";
let nbrLigne = 6;
for(let i=1; i<nbrLigne; i++){
    for (let j=0; j<i; j++){
        console.log(etoile);
    }
     etoile+= " * ";
   
}