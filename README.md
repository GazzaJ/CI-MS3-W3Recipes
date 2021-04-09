[![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/GazzaJ/CI-MS3-W3Recipes)

![W3 Recipes](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/readme-header_1.jpg "W3Recipes")

# [**W3 Recipes**](https://ci-ms3-w3recipes.herokuapp.com/)


As a keen cook, I love to try new recipes, but equally as a regular cook it can sometimes be difficult to think of new recipes to try which keep the whole family happy. Thus I thought it would be interesting to put a bit of a spin on the typical recipe database and attempt to get a recipe for as many countries in the world as possible, and what better way to do this than to get the site users to post their tried and tested favourite recipes.

Thus the primary intention for this website is to provide user with a database of recipes they can search on route to attempting a new recipe, and to also enble those users to upload their own recipes to share with other site users.

The objective is to achieved the above with a visually appealing, interactive yet intuitive UX, which provides simple consistent navigation and interaction irrespective of the device. Ultimately, I would like this site to be fun, and encourage users to:
 - upload their favourite recipes
 - share the site and encourage their friends to also upload recipes
 - keep track of where they stand in terms of number of recipes uploaded, compared to ther users
 - keep track of our progress "filling the map"


[The live website can be viewed here!](https://ci-ms3-w3recipes.herokuapp.com/)

![Am I responsive images](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/am_i_responsive.jpg "Am I Responsive")

## Table of contents
An automatically generated Table of Contents can be accessed by clicking the README.md menu icon at the start of the README section.  
![TOC](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/toc-alt.png)  

1. [User Experience](#user-experience)
   - [User Stories](#stories)
   - [The 5 Planes](#planes)
   - [Wireframes](#wireframes)
2. [Database Schema](#dbschema)
3. [Features](#features)
3. [Technologies Used](#technologies)
4. [Testing](#testing)
5. [Bugs & Issues](#bugs)
6. [Deployment](#deployment)
7. [Resources](#resources)
8. [Credits](#credits)
    - [Acknowledgements](#acknowledgements)
9. [Technical Support](#technical)
______

## **User Experience (UX)** <a name="user-experience"></a>
In W3 Recipes I have attempted to produce a simple clean and intuitive site which is easy to navigate and simple to use. Despite being spread over many pages, each page has a single purpose related to C.R.U.D functionality. Navigation is achieved with a typical navbar with mobile responsive behaviour. The imageray and typography are also key to 


### **User Stories** <a name="stories"></a>
The following user stories were developed during the planning stages for this site.
1. _As a_ **first time visitor**, _I need to_ **understand the purpose of the site**, _in order to_ **consider exploring the site further**.

2. _As a_ ** first time visitor**, _I need to_ **easily access the recipe collection**, _in order to_ **search for a recipe worth making**.

3. _As a_ **first time visitor**, _I need to_ **quickly and easily register on the site**,  _in order to_ **fully interact with the site**.

4. _As a_ **returning user**, _I need_ **an interface where I can upload and save my recipes**, _in order to_ **share my favourite recipes with other site users**.

5. _As a_ **returning user**, _I need to_ **have the ability to edit or delete a recipe I have uploaded** _in order to_ **make changes to, or remove an out of date or incorrect recipe**.

6. _As a _ **site owner**, _I need to_ **ensure some basic access control to edit and delete functionality**, _in order to_ **prevent unauthorised editing or deletion of user uploaded data**.

7.  _As a _ **site owner**, _I need to_ **promote a product, _in order to_ **promote a preferred product on the site**.
___

### **The 5 Planes of UX** <a name="planes"></a>
The five planes provide a framework to discuss the design and development of this app.

#### **Strategy**  
The purpose of W3 Recipes website is to provide users with a convenient and easy means of searching and sharing (uploading and editting) their favourite recipes. The aim is to try and add a fun spin on the typical recipe website by encoraging the users to upload their favourite recipes from as many different countries from around the World as possible to provide a wide array of recipes, and as a bit of fun to enable them to track progress in this respect using the dashboard.
 - As the site owner and a keen cook I get to share a recipe database with like minded users, and in exchange for the development get some new recipes to try.
 - Users get access to all of those recipes and get to upload and share their recipes with a community of like minded keen cooks.

#### **Scope**  
The key features required for this app to function as designed are centered around CRUD interactions with a MongoDB Atlas cloud database management system.:
 - **Create** or upload a recipe into the database which can then be viewed by all other registered users
 - **Read**, or view all of the recipes stored in the database.
    - The list of recipes can be filtered by country of origin
    - Search functionality enables the user to search the title and ingredient fields for keywords of their choice.
 - **Update** any of their own recipes, to change any of the previously stored content, or add additional information (within the limits of the input form)
 - **Delete** recipes they themselves have uploaded. This functionality is NOT extended to other users recipes.

In order to prevent unwanted editting or deletions of users recipes, the website has been designed with a basic level of security. Thus, to access the full functionality users are required to Sign-up to the App, which provides access to the CRUD functionality.
 - User interactions are tracked and managed through the use of a *"Session Cookie"*
 - Uploads are unlimited, however users can only edit and delete their own previously uploaded recipes
 - Users can elect to provide additional basic informataion about themselves and to subscribe or not

##### Functional Requirements
App functionality is provided through a simple and intuitive, mobile responsive navbar. The navbar menu options increases once a user registers or logs into the website, increasing pootential functionality.
Additional interactive anchor linkls are provided to assist users in navigating to strategic pages.

##### Content Requirements
Much of the content on this site will be provided by users.
Outside of this I have tried to use images of food or food related themes.
I am a keen cook, and having an image of a recipe is just as important as the ingredient list and preparation steps, as it provides an enticing view of the endpoint and helps to whet the users appetite. Thus including images with each recipe is a key component.
The typography selected for this site was also important, and needed to be fun yet functional. I have selected more cursive fonts to try and emulate a recipe notebook style.
I deliberately stuck with a clean and simple, structured layout to make it easy to view  and also edit the content.

A consistent design is provided through Flask/Jinja template inheritance.
Recipe pages have a similat design, and the individual Recipe cards are consistent between the Recipes page and Manage Resipes page.
___

#### **Structure**  
W3Recipes is constructed from 11 distinct pages which are accessed through the main and mobile navbars. Prior to log-in there are only three oprions: Home | Sign-up | Log-in
Once through this initial authentication stage users are presented with the a further six options, from which they are able to interact fully with the site: Recipes | Add Recipes | Manage Recipes | Profile | Dashboard | Sign-out
![Workflow](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/workflow.png "Website workflow")
A further three subdomains enable the user to Add, Edit or Delete recipes.  

##### **Interaction Design**
User interactions on the W3Recipes app can be subdivided into three categories:
 - **Navigation**  
 I have reverted to a conventional, mobile responsive navbar for this project, and this is one of the key elements which anchors each distinct page together.  
  ![Navbar](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/navbar.jpg)  

Navigating through the Recipes is achieved through familiar pagination controls.  
![Pagination](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/pagination.jpg)

I have provided links on several pages to also assist user navigation; these are quick links to :
 - Sign-in
 - Add a Recipe
 - Manage Recipes
   

These buttons provide user feedback by either changing or reversing colours when hovered.

 - **Manipulation**  
 Button colours have been chosen to match the site colours while also providing visual cues to their purpose:
   - Green ![Green Button](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/green-button.jpg)  
 Highlights functions to proceed with changes such as submitting a recipe or confirming changes  

   - Orange ![Orange and Red Buttons](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/orange-button.png)  
 Used as a wanrning, or to indicate an action which will result in data being changed. The image above illustrates the difference between EDIT and DELETE functions.

   - Red ![Red Button](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/red-button.jpg)  
 Highlights a Stop or Cancel function for changes, but more importantly highlight actions which could result in data being permanently removed.  

 - **Data Input**
The primary User inputs are achieved 
Users are able to add and change their data (Recipes or User Profile) using a series of forms
>A key consideration in the early planning stages was the method for inputting the recipe ingredients and preparation steps. I had initially thought about getting the user to input the number of ingredients and then looping through this number to enter each ingredient, one at a time. However this would be problematic, if the user inputs an incorrect number. In this case they might have to restart the process, which would be undesirable. **Thus the goal; has been to make it as easy as possible for the user to input this data.**


##### **Information Design**
Information is provided to users on four key pages; Recipes, Manage Recipes, Profile and Dashboard.
Despite rendering slightly different information the structure of the Recipe and Manage Recipe Pages are deliberately similar.

___

#### **Skeleton** 
The W3 Recipes website comprises three main pages:
 - Landing Page
 - Registration Page for first time visitors to gain access to the content
 - Log-in Page for returning visitors

Assuming the user elects to register they are provided access to the remaining pages
 - Recipes page displays 9 recipe cards on each page
   - Filter and search options provided to reduce the number of recipes displayed
 - Individual Recipe pages providing the full recipe detail
 - A Page to add a new recipe
 - A page for the users to manage (Update or Delete) their recipes
   - Echoes the functionality provided by the Recipes and Add Recipe pages
 - A dashboard to track where recipes are uploaded for

Navigation between pages is provided by a standard and intuitive navbar. 

##### **Interface Design**
The intention was to maintain a clean and consistent interface design, re-using elements and page styles wherever possible.
 - The Recipes page and Manage Recipes page are virtually identical aside from the search and filter elements being removed for managing recipes.  

![Interface Design](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/interface-1.jpg) 

 - Recipe cards have a consistent layout between the Recipes and Manage recipes pages. Each has a Floating Action Button which when clicked takes the user to the next level.

![Interface Design](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/interface-2.jpg)

 - The Add Recipes and Edit recipes pages are also identical in their appearance and structure.

![Interface Design](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/interface-3.jpg)

Flashed messages are displayed at the top of the screen below the navbar

Buttons colours are chosen to reflect their purpose, and anchor links have some interactive response when hovered.

##### **Interaction Design**
User interactions on the W3Recipes app can be subdivided into three categories:
 - **Navigation**  
 I have reverted to a conventional, mobile responsive navbar for this project, and this is one of the key elements which anchors each distinct page together.  
  ![Navbar](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/navbar.jpg)  

Navigating through the Recipes is achieved through familiar pagination controls.  
![Pagination](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/pagination.jpg)

I have provided links on several pages to also assist user navigation; these are quick links to :
 - Sign-in
 - Add a Recipe
 - Manage Recipes
   

These buttons provide user feedback by either changing or reversing colours when hovered.

 - **Manipulation**  
 Button colours have been chosen to match the site colours while also providing visual cues to their purpose:
   - Green ![Green Button](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/green-button.jpg)  
 Highlights functions to proceed with changes such as submitting a recipe or confirming changes  

   - Orange ![Orange and Red Buttons](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/orange-button.png)  
 Used as a wanrning, or to indicate an action which will result in data being changed. The image above illustrates the difference between EDIT and DELETE functions.

   - Red ![Red Button](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/red-button.jpg)  
 Highlights a Stop or Cancel function for changes, but more importantly highlight actions which could result in data being permanently removed.

##### **Navigation Design**
I have used a standard Materialize, mobile responsive navbar for W3Recipes.
The menu items change depending on the users status.
 - New users only see: Home, Sign-up and Log-in
 - Once signed-up users are able to see the full menu list which enables thenm to interact with the whole app.

Additional anchor links have been provided in strategic locations to assist user navigation and provide easy access to certain pages. These are consistently located at the bottom of the content above the footer.
 - Landing Page
 Contains two anchor links prompting the user to sign-up. One located within text of a call to action section in the middle of the page. The second is located at the bottom of the page above the footer

 - Recipes page and Manage Recipes page
 Both have a link to the Add Recipes page, where the user is able to upload a new recipe

 - Profile Page
 Contains a link to the Manage Recipes page where they are able to Edit and Delete the recipes they have previously uploaded.

There should be no requirement for the user to ever have to resort to the Browser BACK button.
 - Error Pages
Each error page uses the template inheritance to provide the users the navbar seen throughout the site. should a user  encounter an unexpected error they are able to easily navigate back to the site without having to use the back button.

##### **Information Design**
The basic concept fopr the information design for W3Recipes is laid out in the following wireframes.

#### Wireframes <a name="wireframes"></a>
Wireframes for the original design concepts were created using Balsamiq.
##### Home Page
The landing page explains the purpose of the site to new and returning users. Functionalioty is limited from this page. Users are only able to Sign-up with a new account or Log-In to an existing account.
A Mini version of the Dachboard is shown to hopefully encourage users to find an empty country and to sign-up in order to provide a recipe for it.
![Landing Page](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/home-page.png "Landing Page Wireframe")

##### Sign-Up Page
Simple Sign-Up page enables the user to create unique log-in credentials based on an alphanumeric Username and alphanumeric Password. Back-end logic tests for duplicate entries. Redirects the user to the Recipes Page on successfully signing up.  
![Sign-Up](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/Sign-up.png "Sign-Up Page Wireframe")

##### Login Page
For returning users there is a separate Log-In page to enable access to the full functionality of the site.  
![Login](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/login-page.png "Log-In Page Wireframe")

##### Main Recipe Page
The Recipe page could be considered one of the key pages on the site. Uses READ functionality to display Recipes and provides the ability to filter Recipes by country or search by keywords. This page has pagination controls which are set to display a specific number of recipes to limit scrolling.
Users can select any recipe and see the full details of that recipe in order to make it.
![Recipes Display](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/recipes-page.png "Recipes Page Wireframe")

>**_The main change here was to incorporate what could have comprised separate pages (About, Map and Gallery) into a single page._**


##### Individual Recipe Page
Provides users with the full recipe detail so thay can check the ingredients and follow the steps to make it.
![Full Recipe](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/full-recipe.png "Full Recipe Wireframe")

##### Add Recipe Page
If the logged in user chooses to upload a recipe they can select "ADD RECIPE" from the navbar, which redirect the user to a page with various input fields where they can populate:
 - Recipe Name
 - An image representative of the recipe
 - Recipe Country
 - Recipe Description
 - Servings
 - Preparation and Cooking Time
 - Ingredients
 - Method

Once complete the recipe is uploaded to the MongoDB Atlas Recipes collection.  
![Add Recipe](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/edit-recipe.png "Add Recipe Wireframe") 

###### Manage Recipes Page
This page is a copy of the Recipes Page, however rather than providing search functionality it displays only the recipes the user has uploaded, and enables the user to **UPDATE** or **DELETE** those recipes.
Edit redirects the user to a page similar to the Full Recipe page but with editting functionality.
Selecting Delete will produce a check modal to double check the deleting request before removing the recipe.  
![Manage](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/edit-recipe.png "Manage Recipes Wireframe")  

##### Edit Recipe Page
If the user selects EDIT on the Manage Recipes page they are redirected to a page displaying the full recipe with their previous inputs pre-filling the various input fields. The user can change as few or as many field s as necessary or if they change their mind there is a option to Cancel the edit.  
![Recipe Edit](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/edit-recipe.png "Edit Recipe Wireframe")


##### Profile Page
The profile page initially renders the basic profile information added on Sign-up. There is a button at the bottom of the profile card to enable the users to access the 'Edit Profile' page where they can customise their profile image and select whether or not to subscribe and provide an email adresss.  
![Profile Page](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/profile-page.png)  


##### Edit Profile Page
Enables the user to add a photo or avatar to their profile, provide their location and subscribe to the website.
I chose not to place the subscribe option on the landing page because until you log in you wouldn't necessarily know whether you wanted to subscribe to the website.
Thus it made sense to me to add this to a profile page  

![Edit Profile](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/edit-profile.png)  

##### Dashboard Page  
The dashboard page enables the users to track how many countries the site has recipes for and also see how they compare to other users in terms of total recipes uploaded.
![Dashboard Page](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/recipe-dashboard.png)  

___
#### **Surface**
The aesthetics of W3Recipes was just as important to me as the functionality. Despite not using a lot of imagery for the app, what I have selected needs to be impactful, yet relaxed and fun to match the overall objective.

##### **Colour Scheme**
I typically find great inspiration for colour schemes on pinterest. For W3Recipes I sought inspiration from the following website (https://mariahalthoff.com/blog/food-themed-color-palettes). Rather than stick to a single palette I have selected some of the colours from three of the palettes which match the browns, greens, oranges and reds in the hero image.  
  
![Colour Scheme](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/colour_palette_1.jpg "Colour Palette") ![Colour Scheme](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/colour-palette_2.jpg "Colour Palette") ![Colour Scheme](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/colour_palette_3.jpg "Colour Palette")

##### **Typography**  
Selecting the correct typography for this site is just as important as the other design aspects. My aim was to find fonts to reflect a more relaxed style, welcoming the user into the site. I also wanted variety to help demarcate different sections of the site. The primary criteria which I used to select the fonts for this app' were:
 - Readability
 - Relaxed Style
 - Weight

I had researched different styles which could be used for food related content:
 - https://www.creativebloq.com/inspiration/10-mouth-watering-restaurant-menu-fonts
 - https://line25.com/fonts/best-fonts-for-food-industry-design  

With these criteria and ideas in mind, I started loading various fonts into my CSS file and experimented with different combinations to find the ones which complemented each other and provided an asthetically pleasing look to the site.
I have used Google fonts for each of my builds to date as it has an extensive library of fonts and is simple and reliable to use.  
![Google Fonts]https://fonts.google.com/?preview.text=Hello%20World!&preview.text_type=custom "Google Fonts"
 After some experimentation I settled on the following font styles:
 - Main Website Title and occasional text (Shrikhand)  
It was important to have a font which was clear and readable. I was also looking for bolder/thicker fornt for impact.  

![Font](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/shrikhand.jpg)  

 - Page headings (Galada)  
For these I was looking for a more relaxed, fun font with a slightly cursive style and a bit of weight.  

![Font](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/galada.jpg)  

 - Recipe Titles (Molle)  
I just had to use this font style! Something about it elicited a positive reaction with me and just seemed to work for the Recipe cards.  

![Font](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/molle.jpg)  

 - Recipe Detail (Happy Monkey)  
Given the recipe notebook style I was trying to achieve I wanted a font which lokked more natural and 'written' than the typical online typography.  

![Font](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/happy-monkey.jpg) 

##### **Imagery** 
I was originally planning on using world map as the primary landing page image but decided against as this would have been confusing. I opted to go with a food montage which was an image I purchased from iStock
>**_I chose this image for the range of food types and the vibrant colour combining some of the greens browns and oranges I was looking to incorporate into the app.

The second image was sourced on the internet while searching for images for a Kebab recipe. It's just a great image which I liked and was keen to incorporate into the app.

Last but certainly not the least was my desire to have a subtle food related background behind the interactive elements. I found a really cool version designed and distributed by freepik. The original version would have been too distracting so I opted to adjust the contrast and colours to fade the image. I also added my logo into the circular gap in the center.
>**_I selected this particular image because it had a range of food types; each one is a decent size and they are not too densely packed._**
______

## **Database Schema** <a name="dbschema"></a>  
W3Recipes uses Mongo DB Atlas, a non-relational database to store and retrieve all of the user input data.
The schema for W3 Recipes is relatively simple and is illustrated below:
![DB Schema](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/db-schema.jpg "DB Schema")

The schema contains four collections, with each collection containing multiple documents. 
 - **Users**
 Stores user data. Initialy populated with username and password and a default profile image when users register on the app. Once logged in users can upload their own image url, specify their town or city. If the user elects to subscribe to the site, they are then able to provide their email address.
> **_I chose to do it this way so users are only required to provide some basic information and can register very easily. Once registered they can decide how much more they want to input at any subsequent point. I believe this simplifies the registration process_**

 - **Countries**
 This collection was populated from JSON file of 254 countries using the MongoDB Compass app, which simplified the transfer of the data into individual documents within the collection. The JSON data was copied from (https://flagpedia.net/download/api) and uses the CDN link provided on the website to display the flags on the recipe cards and pages. The individual UK countries were subsequently added into the collection by myself, as they did not appear in the original JSON file.
 Each document contains two id fields; the Atlas provided id and that provided in the JSOn data. It also contains the country name, an alpha2 field which is the ISO two letter country code and an alpha3 field which is the ISO three letter country code.  
 The alpha2 code is used to render the appropriate countey flag.  

 - **Recipe Category**
 The recipe_category collection contains short documents each defining the type of meal category each recipe might be identified by; such as Breakfast, Brunch, Lunch, Dinner, Desserts, Snacks, Appetisers and Sides. The recipe type documents were populated by myself and can be queried whena recipe is created or edited.
> **_There are many different ways to categorise recipes, but the one selected seems the most appropriate for my application_**
 
 - **Recipes**
 The recipes collection is the largest in the database as it combines user text input with data retrieved from the other collections; all of the user supplied input with fields from the other collections. I have selected what I view as essential fields for a basic recipe app, though clearly many more could be added.
Recipe Ingredients and preparation step data is formatted into an Array by splitting the data using each new line. When queried the data is formatted into a list for display.

___
## **Features** <a name="features"></a>
The following table lists the primary features provided by the W3Recipes app.

### **Existing Features**
|Feature|Description| Image URL |
|:-----:|-----|:----:|
| 001   | Simple registration Process with dedicated sign-up page | [Sign-up Page](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/register.jpg) |
| 002   | Dedicated Log-in screen for returning registered users | [Log-in Page](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/log-in.jpg) |
| 003   | Paginated "Recipes Page" where all recipes are displayed | [Recipes Page](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/recipes.jpg) |
| 004   | Recipe Filter function, filters recipes by country of origin. The image provided shows a search by the country "Wales". | [Recipe Filter ](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/filter.jpg) |
| 005   | Recipes text search function enables text based search on Title, recipe type, country, description and ingredients. The image provided illustrates a text search for all recipe Type "Sides" | [Recipe Text Search](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/search.jpg) |
| 006   | A Full Recipe Page provides complete recipe details | [Full Recipe Page](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/full.jpg) |
| 007   | A form which enables users to upload their own recipes | [Add Recipe Form Page](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/add.jpg) |
| 008   | Manage Recipes Page, from where users have the ability to Edit or Delete their own recipes | [Add Recipe Form Page](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/manage-recipes.jpg) |
| 009   | Edit Recipe Form, enables users to modify all of the firlds for any of the recipes they themsleves have uploaded |  [Edit Recipe](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/edit.jpg) |
| 010   | A Profile page contains user details and subscription preference | [Profile Page](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/profile.jpg) |
| 011   | An Edit Profile page to allow users the ability to Edit profile details and change subscription status | [Edit Profile Page](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/edit-prof.jpg) |
| 012   | Dashboard page displaying number of recipes by country, by user, meal type | [Dashboard Page](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/dash.jpg) |
| 013 | Footer | The footer for this web app contains links to the developers GitHub site and LinkedIn Account. The footer also contains a link to contact the developer via email. |  |

> **_The UK map is provided because the standard Atlas Charts world map only recognises the UK as a country and not the individual countries. Showing the individual countries is only possible by selecting the UK Countries map._**

> **_I have chosen not to provide a contact form for this web app. I believe that being able to contact the developer by email is sufficient for this initial release._**

### **Security Features**
Despite not being explicitly required for this build I have chosen to implement certain security features to provide some protection against unauthorised access to other users data.


 1. User Login
 User registers on the site with a simple username and password. Password gets hashed and salted using Password Hash from the Werkzeug Library.

![Sign-up Page](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/register.jpg)

 2. Session Cookie
 Once a user signs up or log's in a unique session cookie is generated for the duration of their session. Recipe uploads are saved in the database against the session cookie username.  



 3.  Restricted access
 The app logic checks the session cookie and only enables users to Manage (edit/delete) their own uploaded recipes.  

![Restricted Access](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/restricted-1.jpg)

 4.  Restricted access
 I have also attempted to prevent backdoor access to editting recipes from the Recipes or Full Recipe pages.  

![Unauthorised Access](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/restrict-2.jpg)

 5.  Deletion Check
 When a user selects the Delete Recipe button, the app renders a modal with a message to confirm the user wishes to delete thiat particular recipe.  

![Deletion Check](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/delete.jpg)

 6. Profanity Filter
 Analyses user input and replaces any matching profanities with "****"

![Profanity Filter](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/profane.jpg)

### **Features Left to implement**
I have attempted to provide as much initial functionality in this app' as I can in the time available. Despite this there are features I would still like to incorporate:
|   Feature     |     Description      |
|---------------|----------------------|
| Image File Upload  | Ability to upload images from users personal image library as opposed to only using URL's |
| Image Validation | Validate image properties (size, aspect ratio etc) prior to uploading                 |
|Inappropriate image filter| Filter innappropriate images from being uploaded or worse, displayed |
______

## **Technologies Used** <a name="technologies"></a>  

This website has been built using the following core technologies:

##### Core Coding languages

- ![HTML 5](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/html-5-logo.png "HTML5") - HTML5
- ![CSS3](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/css3-logo.png "CSS3") - CSS3
- ![Python](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/Python.png "Python") - Python
- ![Javascript](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/javascript.png "Javascript") - Javascript


##### Integrations

- ![Flask](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/flask.png "Flask") - The project uses the Flask micro-framework and links with jinja to create the webpages
- ![Jinja](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/jinja.png "Jinja") - The project uses the Jinja templating engine
- ![Materialize CSS](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/materialize-css.png "Bootstrap 4") - Materialize CSS
- ![Font Awesome](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/fontawesome-logo.png "Font Awesome") - Font Awesome was the source of all icons.
- ![Google Fonts](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/googlefonts-logo.png "Google Fonts") - Fonts used on the website courtesy of Google Fonts
- ![JQuery](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/jquery.png "JQuery") - The project uses JQuery to simplify DOM manipulation.
- PyMongo

#### Database Management System
- ![MongoDB Atlas](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/mongodb.png "MongoDB Atlas") - MongoDB Altas  
- ![MongoDB Compass](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/mongodb.png "MongoDB Compass") - MondgoDB Compass was used to upload the JSON data to the W3Recipes Cluster  
- ![MongoDB Charts](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/mongodb.png "MongoDB Charts") - MongoDB Charts was used to create the website's dashboard

##### Version Control, storage and hosting

- ![Gitpod](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/gitpod-logo.png "Gitpod logo") - All of the website's code was written in the Gitpod IDE.
- ![Git](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/git-logo.png "git logo") - used for maintaining version control of the saved files.
- ![GitHub](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/github-logo.png "Github logo") - used as the primary repository for storying the files and documentation.
- ![Heroku](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/heroku-logo.png "Heroku logo")  - Deployment site

##### Other

- Dillinger was once again used to edit the markdown required for the README.md and TESTING.md files.
______

## **Testing** <a name="testing"></a>
All of the testing conducted on this app', as well as any bugs encountered and explanations of solutions are documented in the following file:-
# [TESTING.md](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING.md) 

______
## **Database Creation** <a name="database"></a>
This app is connected to a MongoDB Atlas Cluster
The following steps were used to create the MongoDB Project Database, and subsequent Collections
 1. Log in to [MongoDB Atlas](https://mongodb.com)
 2. Start a new Project  

 ![Cluster Creation](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/mongo-project.jpg)  
 
 3. Create a new Cluster  
   a. Shared Cluster (Free) option selected 
 4. Select a Cloud provider
   a. AWS in Ireland Selected
 5. Select Data tier
  a. Basic M0 tier selected for the purposes of this project 
 6. Add a Cluster Name
 7. Click Create Cluster  

 ![Cluster Creation](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/mongo-clusters.jpg)  
 
 8. Database Access (Left hand Menu under the Security Heading)  

 ![Network Access](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/mongo-dbaccess.jpg)  

 9. Add a Database user
 10. Set Network Access (Left hand Menu under the Security Heading)  

 ![Network Access](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/mongo-network.jpg)  
 
 11. Add IP Address  
   a. Allow Access from Anywhere **(Not recommended for full production apps)**
 13. Confirm
 14. Select Clusters under Data Storage  
 The buttons will become active once the Cluster has been provisioned
 15. Click Collections to add a database and start adding documents to your database collections
  a. Provide a Database Name
  b. Add a Name for your first collection of documents
 16. Click "Create"

## **Deployment** <a name="deployment"></a>
All of the files necessary to run this website have been stored in a GitHub repository. If you would like to work on your own version of this site or use it as a template for your own work, you have the option to either fork, or make a clone of the original repo.

### **Forking the GitHub Repository**
By forking the GitHub Repository you can make a copy of the original repository on your GitHub account, which enables you to view and/or make your own changes without affecting the original repository. This can be achieved using the following steps...

- Log in to GitHub and locate the GitHub Repository
- At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
- You should now have a copy of the original repository in your GitHub account.
### **Making a Local Clone**
- Log in to GitHub and locate the GitHub Repository
- Under the repository name, click "Clone or download".
- To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
- Open Git Bash
- Change the current working directory to the location where you want the cloned directory to be made.
- Type git clone, and then paste the URL you copied in Step 3.

### **Heroku app creation**
As this is a full-stack website it has been deployed to Heroku.com using the following procedure:
- Log in to Heroku.com
- From the Dashboard, select the "New" button on the Top-Right of the screen
  - Select "Create new app"  

![Heroku]https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/heroku-app.jpg  

- Insert your app name
  - Heroku will let you know whether your chosen name is available
- Select the most appropriate region for your location
- Click the "Create app" button

### **Heroku Deployment**
The above steps will automatically bring you to the "Deploy" tab of your new app.  
![Deployment](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/heroku-github.jpg)

 1. In the "Deployment Method" section select Github  
 Once selected a Connect to GitHub section will display below

![Deployment](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/heroku-app-menu.jpg)  

 2. Ensure your profile is displayed
    - If not type in your GitHub username

![Heroku + Github Repo](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/heroku-repo.jpg)  

 3. Search for, and select the Repo corresponding to the Heroku app
 4. Click "Connect"

This app uses connec and Heroku requires these in order for the website to function as desired. To do this you need to set the Config Vars
 - Under the "Settings" tab, in the Config Vars section select the "Reveal Config Vars" button.  

![Config Vars](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/heroku-config-vars.jpg)  

This will reveal a form for inputting the key and value pairs necessary to connect to the app.

|  KEY  |  VALUE  |
|:-----:|:-------:|
|   IP  | 0.0.0.0 |
|  PORT |  5000   |
| SECRET KEY | Randomly Generated Fort Knox Key|
| MONGO_URI | Your unique MongoDB URI |
| MONGO_DBNAME | Your unique Mongo DB name |

The above Mongo_URI variable can be found in the appropriate Mongo DB Project under Cluster by selecting "Connect"
 1. Select "Clusters"
 2. Select "Connect"
 3. Select "Connect your application"
 4. Choose your Driver and Version
   - **Remember to substitute in your own DBNAME and Password**
 5. Copy your connection string

### **Enabling Automatic Deployment**
 - Select the Heroku "Deploy" tab
 - In the "Automatic deploys" section select the branch you wish to use
 
**There is no difference between the developed version of W3Recipes and that deployed on Heroku**
______

## **Resources** <a name="resources"></a>

I have attempted to work independently as much as possible while building this website, choosing to solve my own issues, using web resources wherever possible. Thus, my main resource throughout this project was again the trusty Google search.
 Aside from Google I have made use of the following resources: -

- [Balsamiq](https://balsamiq.com/wireframes/) – Wireframing Tool
- Code Institute course material and Walkthrough projects
- Google DevTools - for trouble shooting and first pass testing
- Google Lighthouse - Website performance testing
- [StackOverFlow](https://stackoverflow.com/) – Web based coding tips
- [W3Schools](https://www.w3schools.com/) – General coding resource
- [Pexels](https://www.pexels.com/) – Licence free image repository
- [BeFunky](https://www.befunky.com/create/resize-image/) – Online image resizer
- [W3C Validator](https://validator.w3.org/) - HTML and CSS Validation tool
- [JSHint](https://jshint.com/) - Javascript code analysis tool
- [JSLint](https://jslint.com/) - Javascript code quality analysis tool
- [](https://www.tutorialspoint.com/online_python_formatter.htm) - Python code beautifier
- []() - Python PEP8 validation
- [SEO Site Checkup](https://seositecheckup.com/tools/custom-404-error-page-test) - Checks to see if you have a custom 404 page
- [Online Javascript Beautifier](https://codebeautify.org/jsviewer) - Useful tool for indenting JS code
- [Am I responsive?](http://ami.responsivedesign.is/) - Provides a simple view of a websites responsiveness.
- [Responsinator](https://www.responsinator.com/) - Fairly comprehensive responsiveness testing

______

## **Credits** <a name="credits"></a>

### **Content**
The content of this website was created by Gareth John. Snippets of code have been copied from official documentation and other sources creditted below and in the respective code files. All pre-loaded recipes were written by the developer.

### **Media**

The photos used in this site, or in pre-populated recipes by the developer were obtained from the folloing sources:
| Photo | Description | Source | Attribution |
|-------|-------------|--------|-------------|
| 001   | [App Logo](https://www.freelogodesign.org/manager) | Free Logo Design | Designed by the developer |
| 002   |Hero image on landing page| iStock | nitrub Purchased from iStock |
| 003   | [Shish Kebab](https://www.pexels.com/photo/food-plate-restaurant-dinner-5175623/) | Pexels | Shameel Mukkath |
| 004   | [Background images](https://www.freepik.com/free-vector/hand-drawn-delicious-food-background_5107183.htm#page=1&query=food%20background&position=0)| freepik | Pikisuperstar |
| 005   | [Kofta Kebab](https://cdn.pixabay.com/photo/2015/08/20/15/15/grill-897553_960_720.jpg) | Pixabay | No Attribution Required |
| 006   | [Welsh Cakes](https://cdn.pixabay.com/photo/2018/10/05/14/55/cake-3726058_960_720.jpg) | Pixabay | No Attribution Required |
| 007   | [Lamingtons](https://upload.wikimedia.org/wikipedia/commons/c/c5/Mocha_Flake_amingtons.jpg) | Wikimedia Commons | Andy Cavell |
| 008   | [Falafel](https://pixabay.com/photos/falafel-middle-east-chickpeas-2073685/) | Pixabay | No Attribution Required |
| 009   | [Guacamole](https://pixabay.com/photos/avocados-guacamole-drink-food-386795/) | Pixabay | No Attribution Required |
| 010   | [Yorkshire Pudding](https://pixabay.com/photos/food-refreshment-yorkshire-puddings-3264773/)    | Pixabay | No Attribution Required |
| 011   | [Baked Lemon Potatoes](https://i.imgur.com/ajVnWhr.jpg) | Imgur | No Attribution Required |
| 012   | Recipe Image     |         |  |
| 013   | Recipe Image     |         |  |
| 014   | Recipe Image     |         |  |
| 015   | Recipe Image     |         |  |
| 016   | Recipe Image     |         |  |


### **Code Snippets**
Much of the structure of this site follows what was taught during the Backend Development - Task Manager walkthrough project provided by Code Institute, but has been heavily modified to suit a recipe database site with additional functionality not provided in the walkthrough.

 | Code Snippet | Description | Source |
 |:-------:|-------------|:------:|
 |Animated Arrows| Animated arrows in the Landing Page call to action | https://freefrontend.com/css-arrows/#animated-arrows|
 |Remove blank lines and spaces from text inputs | Ensure that if users entered blank lines into the ingredients and methods they could be removed to maintain a neat list | https://www.kite.com/python/answers/how-to-remove-empty-lines-from-a-string-in-python |
 | Country Flag CDN | Code snippet required to programatically embed flags into the website | https://flagpedia.net/download/api |
 | Image url display | Display the image when the url is provided in a textbox | https://stackoverflow.com/questions/31398473/load-image-in-div-from-url-obtained-from-a-text-box/31398762|

### **Acknowledgements** <a name="acknowledgements"></a>

 - Thanks as always to everyone at the Code Institute for the excellent video tutorials and fantastic introduction to Python, Flask and some of the different databases structures. Tim Nelson's Walkthrough projects were particularly enjoyable.
 - Grateful thanks to Tutor support who were on hand when most needed to provide assistance.
 - Thanks to Ed Bradley for hosting a very helpfull MS3 Planning Call and for providing some much needed support along the way.
 - Thanks also to Can Sucullu for opening my eyes to potential vunerabilitis and potential back doors in my web app. 
______
### **Technical Support** <a name="technical"></a>
If you encounter any issues with this website, or require any support please email the developer [johnge71@gmail.com](mailto:johnge71@gmail.com)