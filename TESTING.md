# [**W3 Recipes Testing & Bug Fixes**](https://ci-ms3-w3recipes.herokuapp.com/)
This document records all of the manual testing conducted on the W3Recipes app', and also lists the bugs and fixes recorded during the development of the app'.
The philosophy I have used throughout this build is to code, review and test each part of the website as I progressed, relying heavily on Google Dev tools throughout, for first pass testing.
______
## Table of contents
1. [User Story Teesting](#user-story-testing)
2. [Functionality Testing](#functionality)
   - [Navigation Testing](#first-navigation)
   - [Registration / Log-in](#registration)
   - [Recipe Search & View](#recipes)
   - [Adding a Recipe](#add-recipe)
   - [Edit a Recipe](#edit-recipe)
   - [Delete a Recipe](#delete-recipe)  
3. [Security Testing](#security)
4. [Usability Testing](#usability)
5. [Responsiveness Testing](#responsiveness)
6. [Performance Testing](#performance)
7. [Code Quality & Validation](#code-validation)
8. [Bugs & Issues](#bugs-issues)  

______

### **User Story Testing** <a name="user-story-testing"></a>
The following testing has been carried out to validate how the website addresses each of the user stories:
|User Story|Desctiption|Testing|
|:--------:|-----------|-------|
| 1 |_As a_ **first time visitor**, _I need to_ **understand the purpose of the site**, _in order to_ **consider exploring the site further**|The landing pageexplains the purpose of the site in both text and imagery. instances of a recipe card and the world map from the dashboard have also been included |  

![User Story 1](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/user-story-1.jpg)


|User Story|Desctiption|Testing|
|:--------:|-----------|-------|
| 2 |_As a_ **first time visitor**, _I need to_ **quickly and easily register on the site**,  _in order to_ **fully interact with the site**| There are three links on the Landing page from which any first time user can access the registration page. The registration process is very simple and only requires a username and password |  

![User Story 2](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/user-story-2.jpg)


|User Story|Desctiption|Testing|
|:--------:|-----------|-------|
| 3 |_As a_ **first time visitor**, _I need to_ **easily access the recipe collection**, _in order to_ **search for a recipe worth making**| Once signed-up a new user is immediately redirected to the main recipes page where they have the ability to browse, filter and search the recipes and choose which recipe they would like to see in more detail |  

![User Story 3](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/user-story-3.jpg)


|User Story|Desctiption|Testing|
|:--------:|-----------|-------|
| 4 |_As a_ **returning user**, _I need_ **an interface where I can upload and save my recipes**, _in order to_ **share my favourite recipes with other site users**| An **"Add Recipe"** page has been provided and is clearly indicated on the navbar. This redirects the user to an intuitive form where they can input pre-defined recipe criteria like ingredients and preparation steps |  

![User Story 4](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/user-story-4.jpg)  


|User Story|Desctiption|Testing|
|:--------:|-----------|-------|
| 5 |_As a_ **returning user**, _I need to_ **have the ability to edit or delete a recipe I have uploaded** _in order to_ **make changes to, or remove an out of date or incorrect recipe**||

![User Story 5](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/user-story-5a.jpg)  
![User Story 5](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/user-story-5b.jpg)
![User Story 5](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/user-story-5c.jpg)

|User Story|Desctiption|Testing|
|:--------:|-----------|-------|
| 6 |_As a _ **site owner**, _I need to_ **ensure some basic access control to edit and delete functionality**, _in order to_ **prevent unauthorised editing or deletion of user uploaded data**|Users are only able to view their own recipes on the Manage Recipes page. Users will be redirected to the Manage Recipes Page if they try to manipulate a url from a Full Recipe view to an Edit Recipe view|

![User Story 6](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/user-story-6a.jpg)  
![User Story 6](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/user-story-6b.jpg)  


|User Story|Desctiption|Testing|
|:--------:|-----------|-------|
| 7 |_As a _ **site owner**, _I need to_ **have a unique feature which generates some competition, _in order to_ **encourage users to post new recipes**.| One of the key drivers with W3Recipes is to to try and fill in the map of the world by uploading recipes from as many countries as posible. THe maps are displayed on the Landing page and in a Dashboard Page| 

![User Story 7](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/user-story-7.jpg)
  
______

### **Functionality Testing** <a name="functionality"></a>
The following tables capture the functional testing performed on the web-app to ensure it works as desired. I have tested on the listed browsers only, using Windows version 1909 (OS Build 18363.1256), and have not conducted any backward compatibility testing in older browser versions.  

#### **First Time Navigation Testing** <a name="first-navigation"></a>
Tests the initial navbar selections _( Home | Sign-up | Log-in )_ and various anchor links provided to assist users navigating between pages.

|   Test | Purpose         | Desired Result | Actual Result | Chrome v 89.0.4389.82 | Firefox v 84.0 (64-bit) |
|:------:|-----------------|----------------|---------------|:---------------------:|:-----------------------:|
|   001  | Sign-up Link on Navbar |Correctly navigate to sign-up page | Opens Sign up/registration age | **PASS** | **PASS** |
|   002  | Sign-up Link on Log-in Page |Correctly navigate to sign-up page| Opens Sign up/registration Page  | **PASS**  | **PASS** |
|   003  | Sign-up Link on Landing Page |Correctly navigate to sign-up page| Opens up the Sign-up Page | **PASS** | **PASS** |
|   004  | Sign-up Link on the base of the landing page |Correctly navigate to sign-up page| Opens the Sign-up Page | **PASS** | **PASS** |
|   005  | Log-in Link on Navbar |Correctly navigate to Log-in Page | Redirects user to Log-in Page | **PASS** | **PASS** |
|   006  | Log-in Link on Sign-up Page |Correctly navigates to Sign-up Page | Redirects user to Sign-up/registration page | **PASS**  | **PASS** |
|   007  | Home Link on navbar |Correctly redirects users to the Home Page | Redirects to Home Page | **PASS** | **PASS** |
|   008  | Brand Logo on navbar |Correctly redirects users to the Home Page | Redirects to Home Page | **PASS** | **PASS** |

___

#### **Registration/Log-in Testing** <a name="registration"></a>
Testing the registration process required to Sign-in and create a new account; as well as for returning users to Log-in to their existing account. The app should provide feedback to the user in cases where incorrect inputs are provided. 

|   Test   | Purpose         | Desired Result | Actual Result | Chrome v 87.0.4280.88 | Firefox v 84.0 (64-bit) |
|:--------:|-----------------|----------------|---------------|:------:|:-------:|
|   001    |Username - special Characters not allowed | Indicate requirements not met  | Input box turns red and tooltip provides feedback | **PASS** | **PASS** |
|   002    |Password - special Characters not allowed | Indicate requirements not met  | Input box turns red and tooltip provides feedback | **PASS** | **PASS** |
|   003    |Minimum Character limit (5) | Indicate requirements not met | Input box turns red and tooltip provides feedback | **PASS** | **PASS** |
|   004    | Max character limit (15) | Indicate requirements not met | User input is limited to 15 characters | **PASS** | **PASS** |
|   005    |  Username already taken | Let user know username is taken | User Redirected to Sign-up page with a Flashed message | **PASS** | **PASS** | 

![Username taken](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/username-taken.jpg)

|   Test   | Purpose         | Desired Result | Actual Result | Chrome v 87.0.4280.88 | Firefox v 84.0 (64-bit) |
|:--------:|-----------------|----------------|---------------|:------:|:-------:|
|   006    | Username or password too short | Indicate requirements not met | Input box turns red and tooltip provides feedback | **PASS** | **PASS** |
|   007    | Incorrect Username  | Inform user of issue | User Redirected to Log-in page with a Flashed message | **PASS** | **PASS** |
|   008    | Incorrect Password  | Inform user of Issue | User Redirected to Log-in page with a Flashed message | **PASS** | **PASS** |

![Incorrect Log-in](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/incorrect-login.jpg)

|   Test   | Purpose         | Desired Result | Actual Result | Chrome v 87.0.4280.88 | Firefox v 84.0 (64-bit) |
|:--------:|-----------------|----------------|---------------|:------:|:-------:|
|   009    | Successful Sign-up  | User redirected into web-app with Success message displayed | User is taken to Recipes page with Welcome message displayed | **PASS** | **PASS** |
|   010    | Successful Log-in  | User redirected into web-app with Success message displayed | User is taken to Recipes page with Welcome message displayed | **PASS** | **PASS** |  

![Sign-up Success](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/success-login.jpg)

___


#### **Recipe Search & View (READ)** <a name="recipes"></a>
This section documents the testing performed to validate the ability of the user to view the recipe collection, Filter by country and performa text search. Clicking the action button on each recipe should reveal the full recipe details.
|   Test | Purpose         | Desired Result | Actual Result | Chrome v 89.0.4389.82 | Firefox v 84.0 (64-bit) |
|:------:|-----------------|----------------|---------------|:---------------------:|:-----------------------:|
|  001   |  Latest First  | Display recipes in reverse chronological order | Recipes are sorted, newest to oldest | **PASS** | **PASS** |
|  002   |  Recipe Filter  | Returns results based on user selected country | Correctly filters recipes and only returns matching recipes | **PASS** | **PASS** |
|  003   |  Recipe Filter  | Filter options available after initial search | The Filter function can be used again and again based on different coutries | **PASS** | **PASS** |  

![Country Filter](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/country-filter.jpg)  
![Filter Results](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/filtered-results.jpg)

|   Test | Purpose         | Desired Result | Actual Result | Chrome v 89.0.4389.82 | Firefox v 84.0 (64-bit) |
|:------:|-----------------|----------------|---------------|:---------------------:|:-----------------------:|
|  004   | Recipe Search   | Returns results based on user text input | Recipes displayed based on matching text | **PASS** | **PASS** |

![Recipe Search](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/search-results.jpg)

|   Test | Purpose         | Desired Result | Actual Result | Chrome v 89.0.4389.82 | Firefox v 84.0 (64-bit) |
|:------:|-----------------|----------------|---------------|:---------------------:|:-----------------------:|
|  005   | Recipe Display   | Correctly display the selected recipe in full | Full recipe displayed for respective recipe cards | **PASS** | **PASS** |
|  006   | Pagination | Limits display to 6 recipes | Six recipes displayed per page (where applicable) | **PASS** | **PASS** |
|  007   | Pagination | Next and Previous Page arrows assit navigaction through pages | Next and PRevious page arrows work as desired | **PASS** | **PASS** |
|  008   | Pagination | Page numbers link to respective reciupe page | Recipes displayed based on matching text | **PASS** | **PASS** |
|  009   | Return to main Recipes Page   | No requirement to use the back button | Users can navigate away from the full recipe page using navbar or "Back to Recipes" button at the bottom of the page | **PASS** | **PASS** |
___
   
#### **Add Recipe (CREATE)** <a name="add-recipes"></a> 
Tests to check the users ability to upload a new recipe to the collection, and validate process robustness.
|   Test | Purpose         | Desired Result | Actual Result | Chrome v 89.0.4389.82 | Firefox v 84.0 (64-bit) |
|:------:|-----------------|----------------|---------------|:---------------------:|:-----------------------:|
|  001   | Navbar link   | "Add Recipe" on navbar results in correct page displaying | Users are correctly redirected to the Add Recipe page | **PASS** | **PASS** |
|  002   | Manage Recipe link   | Link provided on Manage Recipes page results in correct page displaying | Users are correctly redirected to the Add Recipe page | **PASS** | **PASS** |
|  003   | Country Select   | Displays the list of countries in alphabetic order | List is displayed in the correct order. Users can scroll, or type the first letter of the country to navigate the list | **PASS** | **PASS** |
|  004   | Recipe Name   | Textbox functions as desired | Users can input a name. Feedback is provided if the name is <5 characters | **PASS** | **PASS** |
|  005   | Category Select  | Displays the list of recipe categories | List displays and users can select the category appropriate for their recipe | **PASS** | **PASS** |
|  006   | Vegetarian / Vegan Switches | Switches are "off" by default and will toggle on when selected. User feedback provided | Switches toggle as desired and change colour to teal when "on" | **PASS** | **PASS** |
|  007   | Servings  | Displays a list of numbers from 1 - 30 | correctly displays the list and is selectable | **PASS** | **PASS** |
|  008   | Recipe Image   | "Add Recipe" on navbar results in correct page displaying | Users are correctly redirected to the Add Recipe page | **PASS** | **PASS** |
|  009   | Prep & Cooking Time   | "Add Recipe" on navbar results in correct page displaying | Users are correctly redirected to the Add Recipe page | **PASS** | **PASS** |
|  010   | Recipe Description   | "Add Recipe" on navbar results in correct page displaying | Users are correctly redirected to the Add Recipe page | **PASS** | **PASS** |
|  011   | Prep & Cooking Time   | "Add Recipe" on navbar results in correct page displaying | Users are correctly redirected to the Add Recipe page | **PASS** | **PASS** |
|  012   | Prep & Cooking Time   | "Add Recipe" on navbar results in correct page displaying | Users are correctly redirected to the Add Recipe page | **PASS** | **PASS** |
|  013   | Data Written to MongoDB   | Confirm new recipe data is written to MongoDB | New recipes appear as a new Recipes document within Mongo DB. All fields are populated if completed | **PASS** | **PASS** |
|  014   | Profanity Check  | Replace profanities in user input with ***  | Profanities are correcxtly replaced with *** | **PASS** | **PASS** |

___

#### **Edit Redipe (UPDATE)** <a name="edit-recipe"></a>

|   Test | Purpose         | Desired Result | Actual Result | Chrome v 89.0.4389.82 | Firefox v 84.0 (64-bit) |
|:------:|-----------------|----------------|---------------|:---------------------:|:-----------------------:|
___

#### **User Profile (READ)** <a name="user-profile"></a>

|   Test | Purpose         | Desired Result | Actual Result | Chrome v 89.0.4389.82 | Firefox v 84.0 (64-bit) |
|:------:|-----------------|----------------|---------------|:---------------------:|:-----------------------:|
___

#### **Edit Profile** <a name="edit-profile"></a>

|   Test | Purpose         | Desired Result | Actual Result | Chrome v 89.0.4389.82 | Firefox v 84.0 (64-bit) |
|:------:|-----------------|----------------|---------------|:---------------------:|:-----------------------:|
___

#### **Delete Recipe (DELETE)** <a name="delete-recipes"></a>  
Testing to confirm correct functionality of the Delete function. Aspects of this testing are critical as we don't want to delete the incorrect recipes.
|   Test | Purpose         | Desired Result | Actual Result | Chrome v 89.0.4389.82 | Firefox v 84.0 (64-bit) |
|:------:|-----------------|----------------|---------------|:---------------------:|:-----------------------:|
| 001    | Navigate to Delete option | Delete button initiates recipe deletion | Clicking Delete correctly initiates the deletion process | **PASS** | **PASS** |

![Start Deletion](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/del-step1.jpg)

|   Test | Purpose         | Desired Result | Actual Result | Chrome v 89.0.4389.82 | Firefox v 84.0 (64-bit) |
|:------:|-----------------|----------------|---------------|:---------------------:|:-----------------------:|
| 002    | Prevent unauthorised Deleteion | Delete function should only be available to ADMIN and the uploading user | The only recipes shown for users are those they have uploaded themselves | **PASS** | **PASS** |
| 003    | Check with user before deleting recipe | Deletion modal should appear, to confirm deletion | Modal appears with confirmation message and Recipe name displayed | **PASS** | **PASS** |

![Start Deletion](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/del-step2.jpg)

|   Test | Purpose         | Desired Result | Actual Result | Chrome v 89.0.4389.82 | Firefox v 84.0 (64-bit) |
|:------:|-----------------|----------------|---------------|:---------------------:|:-----------------------:|
| 004    | Provide escape route | Buton provides way back tgo Manage Recipes | A "Go Back" button has been provided as an alternative to the Confirm Deletion option. redirects user to Manage recipes | **PASS** | **PASS** |
| 005    | Delete Correct Recipe | Ensure the correct recipe is deleted |Each recipe is linked by it's unique id, which is used when selecting or deleting recipes. Confirmation message includes the recipe name. Checked in MongoDB | **PASS** | **PASS** |
| 006    | Provide Confirmation of Deletion | Flash message should appear when user is redirected to Manage Recipes page | User is redirected and message is diaplayed | **PASS** | **PASS** |

![Start Deletion](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/del-confirmation.jpg)
______

### **Code Quality and Validation** <a name="code-validation"></a> 
Online tools have been used to validate the HTML, CSS, Python and JavaScript files to ensure they are free from errors, and comply with the latest standards. The results of these tests are documented below. 

|Test|Process|Result| Comment |
|----|-------|:----:|---------|
|HTML Validation| Copy Index.html code into W3C validator|PASS||
|HTML Validation| Copy Map.html code into W3C validator|PASS||
|HTML Validation| Copy Contact.html code into W3C validator|WARNING|The "type" is unnecessary for Javascript results from 3rd party Script tags|
|HTML Validation| Copy 404.html code into W3C validator|PASS||
|CSS Validation| Copy CSS code into WC3 validator| **CHECKED** || 
|Python Validation| Copy app.py code into [PEP8 Online](http://pep8online.com/)| **CHECKED** | No Errors detected|
|Python Validation| Copy app.py code into [PEP8 Online](http://pep8online.com/)| **CHECKED** | No Errors detected|
|Javascript Validation| Copy script.js code into JSHint | **CHECKED** ||
|Javascript Validation| Copy script.js code into JSLint | **CHECKED** ||

- This project has been deployed using Heroku and the website has been reviewed on several real devices:
  - Samsung Galaxy S9
  - Samsung Tab A
  - HP Laptop with attached monitor
This helped me make some changes to maintain responsiveness. 

- Spelling Checked using [Typosaurus](https://typosaur.us/)
- [CSS Auto Prefixer](https://autoprefixer.github.io/) - CSS file checked 
- Mobile Friendly Test - [PASS](https://search.google.com/test/mobile-friendly?id=8jZoJWUliCuw3Bdmly-IwA)
- README.md file spelling checked by copying and pasting the text into word.


### **Usability Testing** <a name="usability-testing"></a>"
I requested fellow CI students and former colleagues to test the website to gather their feedback on the User Experience and Interactivity. What follows are the comments I received in return:


### **Responsiveness Testing** <a name="responsiveness-testing"></a>
I have conducted continuous responsiveness testing, right up to the final submission, to ensure the website functions on different devices and in both portrait and landscape orientation, using Google Devtools and Responsinator.com.
The table below contains links to the Responsinator results where applicable.
> None of the Responsiveness Tools provided results for pages where user authentication is important, such as Manage Recipes, Edit Recipe, Profile and Edit Profile. I have thus included screenshots of these from Google Devtools.  

|  Test  | Page | Responsinator Link | Result |
|--------|------|--------------------|--------|
|  001   | Landing | [Landing Page](https://www.responsinator.com/?url=https%3A%2F%2Fci-ms3-w3recipes.herokuapp.com%2F) | Page functions across multiple devices in both portrait and landscape |
|  002   | Sign-up | [Sign-up](https://www.responsinator.com/?url=https%3A%2F%2Fci-ms3-w3recipes.herokuapp.com%2Fregister) | Page functions across multiple devices in both portrait and landscape |
|  003   | Log-in | [Log-in](https://www.responsinator.com/?url=https%3A%2F%2Fci-ms3-w3recipes.herokuapp.com%2Flogin) | Page functions across multiple devices in both portrait and landscape |
|  004   | Recipes Page | [Recipes Page](https://www.responsinator.com/?url=https%3A%2F%2Fci-ms3-w3recipes.herokuapp.com%2Fget_recipes) | Page functions across multiple devices in both portrait and landscape |
|  005   | Full Recipe | [Full Recipe](https://www.responsinator.com/?url=https%3A%2F%2Fci-ms3-w3recipes.herokuapp.com%2Ffull_recipe%2F604103a37084e9c04df5e2e5) | Page functions across multiple devices in both portrait and landscape |
|  006   | Add Recipe | [Add Recipe](https://www.responsinator.com/?url=https%3A%2F%2Fci-ms3-w3recipes.herokuapp.com%2Fadd_recipe) | Page functions across multiple devices in both portrait and landscape |
|  007   | Manage Recipes | - | Unable to text using online tools |
|  008   | Edit Recipe | - | Unable to text using online tools |
|  009   | Profile | - | Unable to text using online tools |
|  010   | Edit Profile | - | Unable to text using online tools |
|  011   | Dashboard | [Dashboard](https://www.responsinator.com/?url=https%3A%2F%2Fci-ms3-w3recipes.herokuapp.com%2Fdashboard) | Page functions across multiple devices in both portrait and landscape |
|  012   | Error Pages | [Error Page](https://www.responsinator.com/?url=https%3A%2F%2Fci-ms3-w3recipes.herokuapp.com%2Fprofile%2Fadminuser) | Page functions across multiple devices in both portrait and landscape |

### **Performance Testing** <a name="performance-testing"></a>
The website has been performance testing using the following tools:
 - Google Lighthouse (Desktop)
  
 
![Google Lighthouse](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/google-lighthouse.png "Google Lighthouse Testing")



 - Google Lighthouse (Mobile)
  
 
![Google Lighthouse](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/google-lighthouse-mobile.png "Google Lighthouse Testing")


______

## **Bugs, Issues and Fixes** <a name="bugs"></a>
The following table explains the bugs and issues encountered while building this website.
|  Issue #   |  Bug or Issue  |  Description  |  Solution  |
|:----------:|:--------------:|---------------|------------|
| 001 |Page width exceeding viewport width|While conducting continuous testing I noticed the website was experienceing a sporadic issue with the page width increasing beyond the viewport width. Initially thought to affect all pages and caused by the moibile responsive navbar | While troubleshooting the issue I realised the problem was confined to my Recipes.html page, and thus couldn't be caused by the navber which is a consistent element on all pages. The only other interactive element on this page was an unused Materialize CSS "FeatureDiscovery" element. After deletion the Page width issue didn't reoccur
| 002 |Delete Confirmation in a modal|When a user selects delete on the "Manage Recipes" page I wanted a confirmation email to display before the recipe could be removed from the website and database. Initial attemps resulted in recipes being deleted one by one in a sequence since the modal was not linked to the specific recipe. This was verified using the {{ recipe title }} and by taking the chance and deleting one of the records | 
| 003 |Displaying Flash messages in a modal| Unable to display Flashed messages in a modal | Resorted to displaying them on the top of the relevant pages. |
| 004 | Favicon 404 on some pages | My chosen Fav icon was not displaying on all pages which inherit from the base,html. The error code was "GET /full_recipe/static/img/favicon.ico HTTP/1.1" 404".| Adding a forward slash to the beginning of the directory address fixed the issue.