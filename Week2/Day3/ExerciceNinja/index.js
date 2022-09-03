let note = [10,15,16,11,18,05,09,16,20,17,12];
let somme = 0;
let moyenne = 0;
for(let i=0; i<note.length;i++){
  somme = somme+note[i];
  moyenne = somme/note.length;
}
console.log("votre myenne est ", moyenne);
if(moyenne<10){
  console.log("echoué");
}
else if (moyenne>10){
  console.log("admis");
}