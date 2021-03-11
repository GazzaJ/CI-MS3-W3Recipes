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

/*----- Check Status of "Subscribed" checkbox -----*/
$(document).ready(function(){
    if ($('#subscribed').is(':checked')) {
        $('#subs-email').show();
    } else {            
        $('#subs-email').hide();
    }
});

/*----- Show Textbox to enter email address -----
----- or hide textbox and remove email address -----*/
$(document).ready(function(){
    $('.switch :checkbox').change(function(){        
        if ($(this).is(':checked')) {
            $('#subs-email').show();            
        } else {
            $('#subs-email').hide();            
        }
    })
});