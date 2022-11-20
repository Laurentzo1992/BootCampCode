
let planetes = ["Sun", "Mercury", "Venus", "Earth", "Mars","Pluto", "Neptune", "Uranus", "Jupiter", "Saturn"];


let colorPlanetesList = ["blue", "red", "orange", "#456","yellow", "grey", "violet", "gray", "purple", "#803"];


let lunes = [0, 0, 0, 1, 2, 5, 14, 27, 79, 82]





for (let i = 0; i < planetes.length; i++) {
    let div1 = document.createElement("div");
    let newContent = document.createTextNode(planetes[i]);
    div1.appendChild(newContent);
    div1.className = (`planet ${i}`) 


    div1.style.marginTop='10px';
    document.body.appendChild(div1);
    let backgroundColor = document.getElementsByClassName("planet")[i].style.backgroundColor = colorPlanetesList[i];


    // Bonus
    let margin_left =80 
    if (lunes[i] != 0){
        for (let a =0; a <lunes[i]; a++){
            margin_left+=60
            let div = document.createElement('div');
            div.classList.add('moon');
            div.style.marginLeft=margin_left + 'px';
            div1.appendChild(div)    
        }
    }
}    