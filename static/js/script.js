/*----- Materialize CSS JQuery Helpers -----*/
$(document).ready(function() {
    $(".sidenav").sidenav({
        edge: "right"
    });
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
function addImage() {
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
function editImage() {
    var url = document.getElementById("image_url").value;
    var image = new Image();
    image.src = url;
    document.getElementById("profile-url-container").appendChild(image);
    document.getElementById("new-img").innerHTML = "New Image";
}

/*----- Display New image when URL provided ----- 
---------- on Edit Profile Pages----------
Adapted from https://stackoverflow.com/questions/31398473/
load-image-in-div-from-url-obtained-from-a-text-box/31398762*/
function userImage() {
    var url = document.getElementById("user_image").value;
    var image = new Image();
    image.src = url;
    document.getElementById("profile-url-container").appendChild(image);
    document.getElementById("prof-img").innerHTML = "New Image";
}

/*----- Check Status of "Subscribed" checkbox ----- 
---------- on the Edit Profile Page -----*/
$(document).ready(function() {
    if ($("#subscribed").is(":checked")) {
        $("#subs-email").show();
    } else {
        $("#subs-email").hide();
    }
});

/*----- Show Textbox to enter email address if user -----
----- wants to subscribe, or hide textbox if not -----*/
$(document).ready(function() {
    $(".switch :checkbox").change(function() {
        if ($(this).is(":checked")) {
            $("#subs-email").show();
        } else {
            $("#subs-email").hide();
        }
    });
});

/*----- Change footer link colour on Hover -----*/
$(document).ready(function() {
    $(".hover").hover(function() {
        $(this).toggleClass("toggle");
    });
});

/*----- Change signup link colour on Hover -----*/
$(document).ready(function() {
    $(".cta-signup").hover(function() {
        $(this).toggleClass("toggle2");
    });
});

/*----- Highlight navbar links on Hover -----*/
$(document).ready(function() {
    $(".navlink").hover(function() {
        $(this).toggleClass("toggle2");
    });
});

/*----- Toggle sign-up link on Hover -----*/
$(document).ready(function() {
    $(".signup-2").hover(function() {
        $(this).toggleClass("toggle3");
    });
});

/*----- Toggle img-url link on Hover -----*/
$(document).ready(function() {
    $(".img-link").hover(function() {
        $(this).toggleClass("toggle4");
    });
});

/*----- Toggle recipes link on Hover -----*/
$(document).ready(function() {
    $(".recipe-link").hover(function() {
        $(this).toggleClass("toggle3");
    });
});

/*----- Possible Solution to iOS Select list Error -----*/
/* https://stackoverflow.com/questions/52850091/materialize-select
-and-dropdown-touch-event-selecting-wrong-item/52851046#52851046-*/
$(document).click(function() {
    $('li[id^="select-options"]').on('touchend', function(e) {
        e.stopPropagation();
    });
});

/*----- Check User Input on Add Recipe Form -----*/
/*-- Adapted from (https://html.form.guide/snippets/
javascript-form-validation-using-regular-expression/)--*/
$('#rec-submit').click(function() {
    /*-- Country Variable --*/
    var country = document.getElementById("country_name").value;
    /*-- Recipe title variable and test vs Regex --*/
    var title = document.getElementById("title").value;
    var titleRegex = /^(?:\s*[a-zA-Z]+){1,5}$/;
    var titleResult = titleRegex.test(title);
    /*-- Recipe Category Variable --*/
    var rec_category = document.getElementById("recipe_category").value;
    /*-- Recipe Servings Variable --*/
    var servings = document.getElementById("servings").value;
    /*-- Recipe Ingredients variable and tests vs Regex --*/
    var ingredients = document.getElementById("ingredients").value;
    var ingRegex = /[@:.,!£$%^&*()]+[\s]+/gm;
    var ingredResult = ingRegex.test(ingredients);
    /*-- Recipe Method variable and test vs Regex --*/
    var method = document.getElementById("method").value;
    var methRegex = /[@:.,!£$%^&*()]+[\s]+/gm;
    var methodResult = methRegex.test(method);
    /*----- Check Country Dropdown -----*/
    if (country == "Choose Recipe Country") {
        alert("Please Select a Country for your Recipe!");
        return false;
    }

    /*----- Check Recipe Title -----*/
    if (titleResult == false) {
        alert("Please correct the Recipe name!\n" +
            "Required:- A-Za-z, between 5-60 Characters");
        return false;
    }

    /*----- Check Recipe Category -----*/
    if (rec_category == "Choose Recipe Category") {
        alert("Please Select a Category for your Recipe!");
        return false;
    }

    /*----- Check Recipe Category -----*/
    if (servings == "Number of serving") {
        alert("Please Select Number or Servings for your Recipe!");
        return false;
    }

    /*----- Check Recipe Ingredients -----*/
    if (ingredResult != false) {
        alert("Please enter valid Recipe ingredient text!\n" +
            "500ml Chicken stock");
        return false;
    }

    /*----- Check Recipe Ingredients -----*/
    if (methodResult != false) {
        alert("Please enter valid Recipe method text!\n" +
            "No special characters allowed");
        return false;
    }
    return true;
});

/*----- Check User Input on Edit Recipe Form -----*/
/*-- Adapted from (https://html.form.guide/snippets/
javascript-form-validation-using-regular-expression/)--*/
$('#edit-save').click(function() {
/*-- Recipe Ingredients variable and tests vs Regex --*/
    var ingredients = document.getElementById("ingredients").value;
    var ingRegex = /[@:.,!£$%^&*()]+[\s]+/gm;
    var ingredResult = ingRegex.test(ingredients);
    /*-- Recipe Method variable and test vs Regex --*/
    var method = document.getElementById("method").value;
    var methRegex = /[@:.,!£$%^&*()]+[\s]+/gm;
    var methodResult = methRegex.test(method);
    /*----- Check Recipe Ingredients -----*/
    if (ingredResult != false) {
        alert("Please enter valid Recipe ingredient text!\n" +
            "500ml Chicken stock");
        return false;
    }

    /*----- Check Recipe Ingredients -----*/
    if (methodResult != false) {
        alert("Please enter valid Recipe method text!\n" +
            "No special characters allowed");
        return false;
    }
    return true;
});