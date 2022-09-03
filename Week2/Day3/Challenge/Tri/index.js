///////////////////////////////////////////////////////////////////////////////
//                            DeCroissant
//////////////////////////////////////////////////////////////////////////////

function triDecroissant(arr) {
  //loop forwards through array:
  for (let i = 0; i < arr.length; i++) {
    //loop through the array, moving forwards:
    //note in loop below we set `j = i` so we move on after finding greatest value:
    for (let j = i; j < arr.length; j++) {
      if (arr[i] < arr[j]) {
        let tmp = arr[i]; //store original value for swapping
        arr[i] = arr[j]; //set original value position to greater value
        arr[j] = tmp; //set greater value position to original value
      };
    };
  };
  return arr;
};

console.log(triDecroissant([10,9,1000,12,-11,3]));
// out//=> [ 1000, 12, 10, 9, 3, -11 ]

///////////////////////////////////////////////////////////////////////////////
//                            Croissant
//////////////////////////////////////////////////////////////////////////////


function triCroissant(tab) {
  //nombre des éléments dans le tableau
  var len = tab.length;       
  var tmp, i, j;                  
  
  for(i = 1; i < len; i++) {
    //stocker la valeur actuelle 
    tmp = tab[i]
    j = i - 1
    while (j >= 0 && tab[j] > tmp) {
      // déplacer le nombre
      tab[j+1] = tab[j]
      j--
    }
    //Insère la valeur temporaire à la position 
    //correcte dans la partie triée.
    tab[j+1] = tmp
  }
  return tab
}
var tab = [5,0,9,1,7,4,2,6,3,8];
triCroissant(tab);
console.log(tab);

//out//=> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

