$(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
    $('.tooltipped').tooltip(); 
    $('select').formSelect();    
    $('.parallax').parallax();
    $('.fixed-action-btn').floatingActionButton();
    $('.modal').modal();
});

/*---------- Display image when URL provided----------*/
function addImage()
{
  var url = document.getElementById("image_url").value;
  var image = new Image();
  image.src = url;
  document.getElementById("image-container").appendChild(image);
}

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

/*----- Show Textbox to enter email address if user -----
----- wants to subscribe, or hide textbox if not -----*/
$(document).ready(function(){
    $('.switch :checkbox').change(function(){        
        if ($(this).is(':checked')) {
            $('#subs-email').show();            
        } else {
            $('#subs-email').hide();            
        }
    })
});
