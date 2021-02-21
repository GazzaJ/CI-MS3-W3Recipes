$(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
    $('.tooltipped').tooltip(); 
    $('select').formSelect();    
    $('.tap-target').tapTarget();
    $('.parallax').parallax();
  });

  //----- Create numbers for "Servings" dropdown list 
  var servings = document.getElementById("servings");
  var numbers;

  for (let i = 1; i <= 31; i++) {
      numbers += "<option>" + i + "</option>";
  }

  servings.innerHTML = numbers