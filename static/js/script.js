/*----- Materialize CSS JQuery Helpers -----*/
$(document).ready(function(){
    $(".sidenav").sidenav({edge: "right"});
    $(".tooltipped").tooltip(); 
    $("select").formSelect();    
    $(".parallax").parallax();
    $(".fixed-action-btn").floatingActionButton();
    $(".modal").modal();
});

/*----- Display image when URL provided ----- 
----------- on AddRecipe Pages----------
Adapted from https://stackoverflow.com/questions/31398473/
load-image-in-div-from-url-obtained-from-a-text-box/31398762*/
function addImage()
{
  var url = document.getElementById("image_url").value;
  var image = new Image();
  image.src = url;
  document.getElementById("image-container").appendChild(image);
}

/*---------- FAB for Recipe Edit & Delete ----------*/
document.addEventListener("DOMContentLoaded", function() {
var elems = document.querySelectorAll(".fixed-action-btn");
var instances = M.FloatingActionButton.init(elems, {
    direction: "left"
});
});

/*----- Display New image when URL provided ----- 
---------- on Edit Recipe Pages----------
Adapted from https://stackoverflow.com/questions/31398473/
load-image-in-div-from-url-obtained-from-a-text-box/31398762*/
function editImage()
{
  var url = document.getElementById("image_url").value;
  var image = new Image();
  image.src = url;
  document.getElementById("edit-img-container").appendChild(image);  
  document.getElementById("new-img").innerHTML = "New Image";
}

/*----- Check Status of "Subscribed" checkbox ----- 
---------- on the Edit Profile Page -----*/
$(document).ready(function(){
    if ($("#subscribed").is(":checked")) {
        $("#subs-email").show();
    } else {            
        $("#subs-email").hide();
    }
});

/*----- Show Textbox to enter email address if user -----
----- wants to subscribe, or hide textbox if not -----*/
$(document).ready(function(){
    $(".switch :checkbox").change(function(){        
        if ($(this).is(":checked")) {
            $("#subs-email").show();            
        } else {
            $("#subs-email").hide();            
        }
    });
});

/*----- Change footer link colour on Hover -----*/
$(document).ready(function(){
    $(".hover").hover(function(){
        $(this).toggleClass("toggle");
    });
});

/*----- Change signup link colour on Hover -----*/
$(document).ready(function(){
    $(".cta-signup").hover(function() {
        $(this).toggleClass("toggle2");
    });
});

/*----- Highlight navbar links on Hover -----*/
$(document).ready(function(){
    $(".navlink").hover(function(){
        $(this).toggleClass("toggle2");
    });
});

/*----- Toggle sign-up link on Hover -----*/
$(document).ready(function(){
    $(".signup-2").hover(function(){
        $(this).toggleClass("toggle3");
    });
});

/*----- Toggle img-url link on Hover -----*/
$(document).ready(function(){
    $(".img-link").hover(function(){
        $(this).toggleClass("toggle4");
    });
});

/*----- Toggle recipes link on Hover -----*/
$(document).ready(function(){
    $(".recipe-link").hover(function(){
        $(this).toggleClass("toggle3");
    });
});