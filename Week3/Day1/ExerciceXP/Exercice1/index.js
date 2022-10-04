//1
alert(document.getElementById('container').innerHTML)
//2
document.getElementsByTagName('li')[0].innerHTML = "Zongo"
//3

//4
let saraparent = document.getElementsByTagName('ul')[1];
let saraNode = document.getElementsByTagName('li')[3];
let remov = saraparent.removeChild(saraNode);



