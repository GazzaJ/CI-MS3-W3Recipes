![W3 Recipes](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/readme-header_1.jpg "W3Recipes")
# [**Testing & Bug Fixes**](https://ci-ms3-w3recipes.herokuapp.com/)
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
![KM Feedback](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/km-feedback-2.jpg)


|User Story|Desctiption|Testing|
|:--------:|-----------|-------|
| 2 |_As a_ **first time visitor**, _I need to_ **quickly and easily register on the site**,  _in order to_ **fully interact with the site**| There are three links on the Landing page from which any first time user can access the registration page. The registration process is very simple and only requires a username and password |  

![User Story 2](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/user-story-2.jpg)
![KM Feedback](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/km-feedback-1.jpg)


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
![Dashboard feedback](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/toto-feedback.jpg)
  
______

### **Functionality Testing** <a name="functionality"></a>
The following tables capture the functional testing performed on the web-app to ensure it works as desired. I have tested on the listed browsers only, using Windows version 1909 (OS Build 18363.1500), and have not conducted any backward compatibility testing in older browser versions.  

#### **First Time Navigation Testing** <a name="first-navigation"></a>
Tests the initial navbar selections _( Home | Sign-up | Log-in )_ and various anchor links provided to assist users navigating between pages.

|   Test | Purpose         | Desired Result | Actual Result | Chrome v 89.0.4389.82 | Firefox v 84.0 (64-bit) |
|:------:|-----------------|----------------|---------------|:---------------------:|:-----------------------:|
|   001  | Sign-up Link on Navbar |Correctly navigate to sign-up page | Opens Sign up/registration age | **PASS** | **PASS** |
|   002  | Sign-up Link on Log-in Page |Correctly navigate to sign-up page| Opens Sign up/registration Page  | **PASS**  | **PASS** |
|   003  | Sign-up Link on Landing Page |Correctly navigate to sign-up page| Opens up the Sign-up Page | **PASS** | **PASS** |
|   004  | Sign-up anchor link on the base of the landing page |Correctly navigate to sign-up page| Opens the Sign-up Page | **PASS** | **PASS** |
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
|   005    |  Username already taken | Let user know username it's taken | User Redirected to Sign-up page with a Flashed message | **PASS** | **PASS** | 

![Username taken](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/username-taken.jpg)

|   Test   | Purpose         | Desired Result | Actual Result | Chrome v 87.0.4280.88 | Firefox v 84.0 (64-bit) |
|:--------:|-----------------|----------------|---------------|:------:|:-------:|
|   006    | Username or password too short | Indicate requirements not met | Input box turns red and tooltip provides feedback | **PASS** | **PASS** |
|   007    | Incorrect Username  | Inform user of issue | User Redirected to Log-in page with a Flashed message | **PASS** | **PASS** |
|   008    | Incorrect Password  | Inform user of Issue | User Redirected to Log-in page with a Flashed message | **PASS** | **PASS** |

![Incorrect Log-in](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/incorrect-login.jpg)

|   Test   | Purpose         | Desired Result | Actual Result | Chrome v 87.0.4280.88 | Firefox v 84.0 (64-bit) |
|:--------:|-----------------|----------------|---------------|:------:|:-------:|
|   009    | Successful Sign-up  | User redirected into web-app with Success message displayed | User is taken to Profile page with Welcome message displayed | **PASS** | **PASS** |
|   010    | Successful Log-in  | User redirected into web-app with Success message displayed | User is taken to Recipes page with Welcome message displayed | **PASS** | **PASS** |  

![Sign-up Success](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/success-login.jpg)

___


#### **Recipe Search & View (READ)** <a name="recipes"></a>
This section documents the testing performed to validate the ability of the user to view the recipe collection, filter by country and perform a text search. Clicking the Floating Action Button on each recipe should reveal the full recipe details.
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
> **The recipe country filter and text search are not able to be used together in this first release of the app.**

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
|  005   | Regex pattern matching | No special characters or continuous spaces| Field highlights red and message displays on hover [BAD MATCH](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/search-results.jpg) [GOOD MATCH](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/search-results.jpg) | **PASS** | **PASS** |
|  006   | Category Select  | Displays the list of recipe categories | List displays and users can select the category appropriate for their recipe | **PASS** | **PASS** |
|  007   | Vegetarian / Vegan Switches | Switches are "off" by default and will toggle on when selected. User feedback provided | Switches toggle as desired and change colour to teal when "on" | **PASS** | **PASS** |
|  008   | Servings  | Displays a list of numbers from 1 - 30 | correctly displays the list and is selectable | **PASS** | **PASS** |
|  009   | Recipe Image   | "Add Recipe" on navbar results in correct page displaying | Users are correctly redirected to the Add Recipe page | **PASS** | **PASS** |
|  010   | Prep & Cooking Time   | "Add Recipe" on navbar results in correct page displaying | Users are correctly redirected to the Add Recipe page | **PASS** | **PASS** |
|  011   | Recipe Description   | "Add Recipe" on navbar results in correct page displaying | Users are correctly redirected to the Add Recipe page | **PASS** | **PASS** |
|  012   | Prep & Cooking Time   | "Add Recipe" on navbar results in correct page displaying | Users are correctly redirected to the Add Recipe page | **PASS** | **PASS** |
|  013   | Prep & Cooking Time   | "Add Recipe" on navbar results in correct page displaying | Users are correctly redirected to the Add Recipe page | **PASS** | **PASS** |
|  014   | Data Written to MongoDB   | Confirm new recipe data is written to MongoDB | New recipes appear as a new Recipes document within Mongo DB. All fields are populated if completed | **PASS** | **PASS** |
|  015   | Profanity Check  | Replace profanities in user input with ***  | Profanities are correcxtly replaced with *** | **PASS** | **PASS** |

___

#### **Edit Redipe (UPDATE)** <a name="edit-recipe"></a>

|   Test | Purpose         | Desired Result | Actual Result | Chrome v 89.0.4389.82 | Firefox v 84.0 (64-bit) |
|:------:|-----------------|----------------|---------------|:---------------------:|:-----------------------:|
|  001   | Edit Recipe Form | Edit Recipe form displays correctly | The form displays and is almost identical to the Add Recipe form | **PASS** | **PASS** |
|  002   | Existing Data renders| Display existing recipe data from the database on the form | All of the existing data is rendered from the database into the form fields | **PASS** | **PASS** |
|  003   | Country of Origin | Country of Origin is populated and selectable | Country of origin dropdown functions and is selectable | **PASS** | **PASS** |
|  004   | Recipe Categories | Recipe Categories are populated and selectable | Category dropdown functions and is selectable | **PASS** | **PASS** |
|  005   | Recipe title is editable | User can change the recipe title | The user can edit and delete the recipe title  | **PASS** | **PASS** |
|  006   | Servings| Servings is populated and selectabple  | Servings dropdown functions and is selectable | **PASS** | **PASS** |
|  007   | Vegan & Vegetarian switches | Function and become highlighted on Recipe card is selected | Switches function and currectly highlight whensaved | **PASS** | **PASS** |
|  008   | Recipe Image | Dsiplays from the start | The recipe image is visible | **PASS** | **PASS** |
|  009   | New Recipe Image | Renders if a valid URL is supplied | The new image displays below the old image | **PASS** | **PASS** |
|  010   | Recipe Description | Description is editable and saves correctly |  | **PASS** | **PASS** |
|  011   | Recipe Ingredients | Ingredients are editable and save correctly |  | **PASS** | **PASS** |
|  012   | Recipe Image | Preparation steps are editable and save correctly |  | **PASS** | **PASS** |
|  013   | Confirmation of Upload | Provide confirmation of upload and redirect the user away from the Edit Recipe form | User is redirected to the manage Recipes page and a confirmatio message  is flashed to the screen | **PASS** | **PASS** |

___

#### **User Profile (READ)** <a name="user-profile"></a>

|   Test | Purpose         | Desired Result | Actual Result | Chrome v 89.0.4389.82 | Firefox v 84.0 (64-bit) |
|:------:|-----------------|----------------|---------------|:---------------------:|:-----------------------:|
|  001   | Render Information correctly | Display the information for the user stored in the DB | Basic information displayed for usaers who haven't edit their profile.  | **PASS** | **PASS** |

![Basic Profile](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/basic-profile.jpg)

|   Test | Purpose         | Desired Result | Actual Result | Chrome v 89.0.4389.82 | Firefox v 84.0 (64-bit) |
|:------:|-----------------|----------------|---------------|:---------------------:|:-----------------------:|
|  002   | Display email | Correctly displays email address if user chooses to subscribe | Email address is rendered below Town / City  | **PASS** | **PASS** |
|  003   | Display city | City name displays correctly if user chosses to supply it | City displays below profile image | **PASS** | **PASS** |
|  004   | Display image | Display updated image if one supplied. Display in Center of form | Image displays correctly in the center of the Profile form | **PASS** | **PASS** |

![Full Profile](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/full-profile.jpg)

|   Test | Purpose         | Desired Result | Actual Result | Chrome v 89.0.4389.82 | Firefox v 84.0 (64-bit) |
|:------:|-----------------|----------------|---------------|:---------------------:|:-----------------------:|
|  005   | Remove Email | Remove email if user unsubscribes | The email is no longer rendered on the Profile page | **PASS** | **PASS** |

![Unsubscribed Profile](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/unsubscribed.jpg)

|   Test | Purpose         | Desired Result | Actual Result | Chrome v 89.0.4389.82 | Firefox v 84.0 (64-bit) |
|:------:|-----------------|----------------|---------------|:---------------------:|:-----------------------:|
|  006   | Edit Profile Button| Redirect the user to the Edit profile page | Users are coirrectly redirected to the Edit Profile page|  |  |
|  007   | Delete Profile Button | Opens up a Confirmation Modal - no deletion yet | Modal appears, Delete function not yet triggered |  |  |
___

#### **Edit Profile** <a name="edit-profile"></a>

|   Test | Purpose         | Desired Result | Actual Result | Chrome v 89.0.4389.82 | Firefox v 84.0 (64-bit) |
|:------:|-----------------|----------------|---------------|:---------------------:|:-----------------------:|
|  001   | Edit Profile image | Profile image updates correctly when new URL supplied |  | **** | **** |
|  002   | City update | Users city is uploaded to database when supplied and new data rendered into profile| Information saves and renders correctly | **PASS** | **PASS** |
|  003   | Subscribed switch functionality | Switch status changes when selecting on and opens email entry input field | Switch functions correctly and email input field appears | **PASS** | **PASS** |

![Subscribed Off](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/subscribed-off.jpg)
![Subscribed On](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/subscribed-on.jpg)
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
|   Test | Purpose         | Desired Result | Actual Result | Chrome v 89.0.4389.82 | Firefox v 84.0 (64-bit) |
|:------:|-----------------|----------------|---------------|:---------------------:|:-----------------------:|
| 007 | Only delete the selected recipe document when performing deletions | Confirm only recipe data is removed from the database on deletion. Ensure no other collectiona are affected by the Delete function. | Only selected document is deleted. No downstream effect; no other collections or documents affected| **PASS** | **PASS** |

To confirm the integrity of the deletion process I chose to deleted a recipe created to validate the profanity filter
The recipe exists in the MongoDB Atlas database prior to deletion.

![Recipe in Database](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/recipe-collection.jpg)

1. Delete the "**** Soup" from the Manage Recipes page
   - This recipe used document fields from other collections
     - User = Adminuser
     - Country = Canada
     - Recipe Category = Appetisers  

 If the deletion process works as desired each of these fields should remain post deletion.
2. Delete confirmation modal appears to check Deletion - **PASS**

![Delete Check](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/confirm-delete.jpg)

3. Once confirmed the user is redirected to the Manage Recipes page - **PASS**
4. A Flash message appears at the top of the Manage Recipes page confirming deletion - **PASS**
5. The recipe no longer appears on the Manage Recipes page - **PASS**

![](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/deleted.jpg)

6. The Recipe has been deleted from the database - **PASS**

![](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/recipe-removed.jpg)

7. The integrity of the other collections has not been affected. - **PASS**

![User Collection](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/user-collection.jpg)
![Country Collection](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/country-coll.jpg)
![Recipe Category Collection](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/recipe-category.jpg)

______

### **Code Quality and Validation** <a name="code-validation"></a> 
Online tools have been used to validate the HTML, CSS, Python and JavaScript files to ensure they are free from errors, and comply with the latest standards. The results of these tests are documented below. 

|Test|Process|Result| Comment |
|----|-------|:----:|---------|
|HTML Validation| Copy page URI into W3C validator|Warnings & Errors| See table below |
|CSS Validation| Copy CSS code into WC3 validator| **CHECKED** | No Errors Detected |
|CSS Beautifier| [CSS Auto Prefixer](https://autoprefixer.github.io/) | **CHECKED** | Output Used |
|Python Validation| Copy app.py code into [PEP8 Online](http://pep8online.com/)| **CHECKED** | No Errors Detected|
|Python Validation| Copy app.py code into [PEP8 Online](http://pep8online.com/)| **CHECKED** | No Errors Detected|
|Javascript Validation| Copy script.js code into JSHint | **CHECKED** ||
|Javascript Validation| Copy script.js code into JSLint | **CHECKED** ||
|Website Spelling | URL input [Typosaurus](https://typosaur.us/) | **CHECKED** | Difficulty on pages requiring authentication so MS Word used |
| README file Spelling | Text copied into word | **CHECKED** |  |

> Where appropriate. Pages specific to user session cookie cannot be checked by external online resources. See below.

#### **HTML Validation**
| Page | Error / Warning | Comment |
|:----:|-----------------|---------|
| Multiple Pages | Possible misuse of Aria-Label| I have looked this up on [MDN](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/ARIA_Techniques/Using_the_aria-label_attribute) and balieve that since there is nothing to explicitly explain the purpose of these buttons/links, using the aria label is justified. |
| Multiple Pages | Lack of a heading | The page has a heading. This is not a conventional website page layout of multiple headed sections. |
| Recipes Page | Duplicate id's (recipe-fab) | Results from re-use of the single recipe card design to render each recipe. Required to achieve positioning. |
| Multiple Pages | Bad value through use of { variable } | Required use with Flask  - justified |
| Edit Profile | Duplicate id="subscribed" | Results from conditional logic - justified use |
| Edit Profile | The label element may contain at most one descendent | Results from conditional logic in code - justified use |

____

### **Usability Testing** <a name="usability-testing"></a>
I requested fellow CI students and former colleagues to test the website to gather their feedback on the User Experience and Interactivity. What follows are the comments I received in return:

____

### **Responsiveness Testing** <a name="responsiveness-testing"></a>
I have conducted continuous responsiveness testing, right up to the final submission, to ensure the website functions on different devices and in both portrait and landscape orientation, using Google Devtools and Responsinator.com.
This project has been deployed using Heroku and the website has been continuously reviewed on several real devices:
  - Samsung Galaxy S9
  - Samsung Tab A
  - HP Laptop with attached monitor
This helped me make some changes to maintain responsiveness.

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

____

### **Performance Testing** <a name="performance-testing"></a>
The website has been performance testing using the following tools:
 - Google Lighthouse (Desktop)  

![Landing Page Lighthouse](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING-img/landing-lighthouse.jpg)

|    Page    | Performance | Accessibility | Best Practices | SEO  |
|:----------:|:-----------:|:-------------:|:--------------:|:----:|
|Landing Page|    97%      |      100%     |       93%      | 100% |
|Recipes Page|    80%      |       85%     |       93%      | 100% |
|Full Recipe |    98%      |       95%     |       93%      | 100% |
| Add Recipes|    82%      |       89%     |       93%      |  90% |
|Manage Recipes|  93%      |       91%     |       93%      |  90% |
| Edit Recipe  |  79%      |       89%     |       93%      | 100% |
| Profile Page |  97%      |       95%     |      100%      | 100% |
| Edit Profile |  97%      |      100%     |      100%      | 100% |
| Dashboard    |  90%      |      100%     |       87%      | 100% |

 - Google Lighthouse (Mobile)  

|    Page    | Performance | Accessibility | Best Practices | SEO  |
|:----------:|:-----------:|:-------------:|:--------------:|:----:|
|Landing Page|      42%    |       97%     |      87%       | 100% |
|Recipes Page|      58%    |       85%     |      93%       | 100% |
|Full Recipe |      61%    |       95%     |      93%       | 100% |
| Add Recipes|      59%    |       89%     |      93%       |  90% |
|Manage Recipes|    69%    |       91%     |      87%       |  92% |
| Edit Recipe  |    67%    |       89%     |      93%       | 100% |
| Profile Page |    86%    |       95%     |      100%      | 100% |
| Edit Profile |    90%    |      100%     |      100%      | 100% |
| Dashboard    |    58%    |      100%     |       87%      | 100% |

____

### **Security Testing** <a name="security-testing"></a>
The following tests have been performed on the limited security features implemented on this site, and are documented in the table below:

|   Test | Purpose         | Desired Result | Actual Result | Chrome v 89.0.4389.82 | Firefox v 84.0 (64-bit) |
|:------:|-----------------|----------------|---------------|:---------------------:|:-----------------------:|
|  001   | Username Reuse  | No username duplication allowed | Sign-up does not allow duplicate usernames. A warning message is flashed onscreen and the user redirected to Sign-in again | **PASS** | **PASS** |
|  002   | Password Security  | Passwords are hashed and salted  | Each user passwords is converted into a unique string of characters | **PASS** | **PASS** |
|  003   | Users can only edit and delete their recipes | Users can only view their own uploads when selecting the Manage Recipes page | The Manage Recipes view is limited to those recipes the user has uploaded |  **PASS** | **PASS** |
|  003   | Prevent unauthorised recipe edits | Prevent users from editting a Full_Recipe URL such as ("https://ci-ms3-w3recipes.herokuapp.com/full_recipe/604105c97084e9c04df5e2e7") and changing full recipe to  edit_recipe. | Users are redirected back to the Manage Recipes page. Warning message flashed to screen. | **PASS** | **PASS** |
|  004   | Prevent unauthorised recipe deletion | Prevent users from editting a Full_Recipe URL such as ("https://ci-ms3-w3recipes.herokuapp.com/full_recipe/604105c97084e9c04df5e2e7") and changing full recipe to delete_recipe.| Users are redirected back to the Manage Recipes page. Warning message flashed to screen. | **PASS** | **PASS** |
|  005   | Profanity Filter | Profanity filter changes all **recognised** profanities to "****" | Checked various words and have added a couple of additional variations which were missing | **PASS** | **PASS** |
|  006   | SSLify | All page requests should be redirected to https | All pages are https | **PASS** | **PASS** |

> **Although the profanity filter aims to recognise as many words as it can it is always vulnerable to creative users who are determined to find weaknesses**
______

## **Bugs, Issues and Fixes** <a name="bugs"></a>
The following table explains the bugs and issues encountered while building this website.
|  Issue #   |  Bug or Issue  |  Description  |  Solution  |
|:----------:|:--------------:|---------------|------------|
| 001 |Page width exceeding viewport width|While conducting continuous testing I noticed the website was experienceing a sporadic issue with the page width increasing beyond the viewport width. Initially thought to affect all pages and caused by the moibile responsive navbar | While troubleshooting the issue I realised the problem was confined to my Recipes.html page, and thus couldn't be caused by the navber which is a consistent element on all pages. The only other interactive element on this page was an unused Materialize CSS "FeatureDiscovery" element. After deletion the Page width issue didn't reoccur
| 002 |Delete Confirmation in a modal|When a user selects delete on the "Manage Recipes" page I wanted a confirmation email to display before the recipe could be removed from the website and database. Initial attempts resulted in recipes being deleted one by one in a sequence since the modal was not linked to the specific recipe. This was verified using the {{ recipe title }} and by taking the chance and deleting one of the records | Not a huge problem as the flashed messages work adequately. I just thought a modal might be a more elegant solution.
| 003 |Displaying Flash messages in a modal| Unable to display Flashed messages in a modal. Unable to combine Flask/Jinja syntax with Materialize Modal when using a loop. | Resorted to displaying them on the top of the relevant pages. Not a significant issue as Flashed messages work well. |
| 004 | Favicon 404 on some pages | My chosen Fav icon was not displaying on all pages which inherit from the base,html. The error code was "GET /full_recipe/static/img/favicon.ico HTTP/1.1" 404".| Adding a forward slash to the beginning of the directory address fixed the issue.|
| 005 | 500 Server Error | The web app responds with a 500 internal server error if you try to use the back button after logging out of the app. This is because the session cookie is cleared on loggout and the main pages require a session cookie. | The solution would be to simply display the home page, but I was unable to figure out how to achieve this in this particular case. |

**[Back to Github Repo](https//:github.com/GazzaJ/CI-MS3-W3Recipes/)**