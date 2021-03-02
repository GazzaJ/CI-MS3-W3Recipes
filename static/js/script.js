$(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
    $('.tooltipped').tooltip(); 
    $('select').formSelect();    
    $('.parallax').parallax();
    $('.fixed-action-btn').floatingActionButton();
    $('.modal').modal();
  });
  
/*---------- FAB for Recipe Edit & Delete ----------*/
document.addEventListener('DOMContentLoaded', function() {
var elems = document.querySelectorAll('.fixed-action-btn');
var instances = M.FloatingActionButton.init(elems, {
    direction: 'left'
});
});

/*---------- Recipe Like Counter ----------*/
var clicks = 1;

document.getElementById("likes").innerHTML = clicks;

$('#thumbs-up').click(function() {
  clicks += 1;
  document.getElementById("likes").innerHTML = clicks;
  /*$('.like-counter').addClass("liked");*/
});