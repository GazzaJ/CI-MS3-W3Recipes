[![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/GazzaJ/CI-MS3-W3Recipes)

![W3 Recipes](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/readme-header_1.jpg "W3Recipes")

# [**W3 Recipes**](https://ci-ms3-w3recipes.herokuapp.com/)


As a keen cook, I love to try new recipes, but equally as a regular cook it can sometimes be difficult to think of new recipes to try which keep the whole family happy. Thus I thought it would be interesting to put a bit of a spin on the typical recipe database and attempt to get a recipe for as many countries in the world as possible, and what better way to do this than to get the site users to post their tried and tested favourite recipes.

Thus the primary intention for this website is to provide user with a database of recipes they can search on route to attempting a new recipe, and to also enble those users to upload their own recipes to share with other site users. The secondary purpose of the site is to provide the site owner with a means to promote a particular product.

The objective is to achieved the above with a visually appealing, interactive yet intuitive UX, which provides simple consistent navigation and interaction irrespective of the device. Ultimately, I would like this site to be fun, and encourage people:
 - to upload their favourite recipes
 - share the site and encourage their friends to also upload recipes
 - keep track of how popular their recipes are
 - keep track of our progress "filling the map"


[The live website can be viewed here!](https://ci-ms3-w3recipes.herokuapp.com/)

![Am I responsive images](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/am-i-responsive.png "Am I Responsive")

## Table of contents
1. [User Experience](#user-experience)
   - [User Stories](#stories)
   - [The 5 Planes](#planes)
   - [Wireframes](#wireframes)
2. [Features](#features)
3. [Technologies Used](#technologies)
4. [Testing](#testing)
   - [User Story Testing](#user-story-testing)
   - [Functionality Testing](#functionality-testing)
   - [Code Validation](#code-validation)
   - [Usability Testing](#usability-testing)
   - [Responsiveness Testing](#responsiveness-testing)
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


### **The 5 Planes of UX** <a name="planes"></a>
The five planes provide a framework to discuss the design and development of this app.

#### **Strategy**  
The purpose of W3 Recipes website is to provide users with a convenient and easy means of searching and sharing (uploading and editting) their favourite recipes. The aim is to try and add a fun spin on the typical recipe website by encoraging the users to upload their favourite recipes from as many different countries from around the World as possible to provide a wide array of recipes, and as a bit of fun to enable them to track progress in this respect using the dashboard.
 - As the site owner and a keen cook I get to share a recipe database with like minded users, and in exchange for the development get some new recipes to try.
 - Users also get access to all of those recipes and get to upload and share their recipes with a community of like minded keen cooks.

#### **Scope**  
The key features required to enable this app to function as designed are centered around CRUD interactions with a MongoDB Atlas cloud database management system.:
 - **Create** or upload a recipe into the database which can then be viewed by all other registered users
 - **Read**, or view all of the recipes stored in the database.
    - The list of recipes can be filtered by country of origin
    - Search functionality enables the user to search the title and ingredient fields for keywords of their choice.
 - **Update** any of their own recipes, to change any of the previously stored content, or add additional information (within the limits of the input form)
 - **Delete** recipes they themselves have uploaded. This functionality is NOT extended to other users recipes.

In order to prevent unwanted editting or deletions of users recipes, the website has been designed with a basic level of security. Thus, to access the full functionality users are required to Sign-up to the App, which provides access to the CRUD functionality.
 - User interactions are tracked and managed through the use of a *"Session Cookie"*
 - Uploads are unlimited, by users can only edit and delete their own previously uploaded recipes
 - Users can elect to provide additional basic informataion about themselves and to subscribe or not

##### Functional Requirements
App functionality is provided through simple navigation using an intuitive, and mobile responsive navbar. The navbarr menu options increases once a user registers or logs into the website, increasing pootential functionality.
One page each to c

##### Content Requirements
Much of the content on this site will be provided by users.
Outside of this I have tried to use images of food or food related themes.
I am a keen cook, and having an image of a recipe is just as important as the ingredient list and preparation steps, as it provides an enticing view of the endpoint and helps to whet the users appetite. Thus including images with each recipe is a key component.
The typography selected for this site was also important, and needed to be fun yet functional. I have selected more cursive fonts to try and emulate a recipe notebook style.
I deliberately stuck with a clean and simple, structured layout to make it easy to view  and also edit the content.

A consistent design is provided through Flask/Jinja templating inheritance.

#### **Structure**  
W3Recipes is constructed from 11 distinct pages which were created using jinja template inheritance. This simplified the basic structure of the site and reduced the need for repetition. It may have been possible to build this with scrollable sections, however as each page tends to have a distinct purpose, it made sense to build individual pages.
Adding and Editing data are very similar and thus the structure and design of some pages have been re-used to create a familiar and intuitive format for the user.

##### Interaction Design
I have reverted to a conventional, mobile responsive navbar for this project, and this is one of the key elements which anchors each distinct page together.
Button colours have been chosen to match the site colours while also providing visual cues to their purpose:
 - Green ![Green Button](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/green-button.jpg)
 Highlights functions to proceed with changes such as submitting a recipe or confirming changes  

 - Orange ![Orange and Red Buttons](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/orange-red-fabs.jpg)
 Used as a wanrning, or to indicate an action which will result in data being changed. The image above illustrates the difference between EDIT and DELETE functions.  

 - Red ![Red Button](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/red-button.jpg)
 Highlights a Stop or Cancel function for changes, but more importantly highlight actions which could result in data being permanently removed.



>A key consideration in the early planning stages was the method for inputting the recipe ingredients and preparation steps. I had initially thought about getting the user to input the number of ingredients and then looping through this number to enter each ingredient, one at a time. However this would be problematic, if the user inputs an incorrect number. In this case they might have to restart the process, which would be undesirable. **Thus the goal; has been to make it as easy as possible for the user to input this data.**
##### Information Design



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

All of these options are provided on a fairly typical and intuitive navbar. 

##### Interface Design


##### Navigation Design




##### Information Design



#### Wireframes <a name="wireframes"></a>
Wireframes for the original design concepts were created using Balsamiq.
##### Home Page
The landing page explains the purpose of the site to new and returning users. Functionalioty is limited from this page. Users are only able to Sign-up with a new account or Log-In to an existing account.
A Mini version of the Dachboard is shown to hopefully encourage users to find an empty country and to sign-up in order to provide a recipe for it.
![Landing Page](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/home-page.png "Landing Page Wireframe")

##### Sign-Up Page
Simple Sign-Up page enables the user to create unique log-in credentials based on an alphanumeric Username and alphanumeric Password. Back-end logic tests for duplicate entries. Redirects the user to the Recipes Page on successfully signing up.  
![Sign-Up](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/Sign-up.png "Sign-Up Page Wireframe")

#### Login Page
For returning users there is a separate Log-In page to enable access to the full functionality of the site.  
![Login](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/login-page.png "Log-In Page Wireframe")

##### Main Recipe Page
The Recipe page could be considered one of the key pages on the site. Uses READ functionality to display Recipes and provides the ability to filter Recipes by country or search by keywords. This page has pagination controls which are set to display a specific number of recipes to limit scrolling.
Users can select any recipe and see the full details of that recipe in order to make it.
![Recipes Display](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/recipes-page.png "Recipes Page Wireframe")

>**_The main change here was to incorporate what could have comprised separate pages (About, Map and Gallery) into a single page._**


###### Individual Recipe Page
Provides users with the full recipe detail so thay can check the ingredients and follow the steps to make it.
![Full Recipe](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/full-recipe.png "Full Recipe Wireframe")

#### Add Recipe Page
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

##### Manage Recipes Page
This page is a copy of the Recipes Page, however rather than providing search functionality it displays only the recipes the user has uploaded, and enables the user to **UPDATE** or **DELETE** those recipes.
Edit redirects the user to a page similar to the Full Recipe page but with editting functionality.
Selecting Delete will produce a check modal to double check the deleting request before removing the recipe.  
![Manage](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/edit-recipe.png "Manage Recipes Wireframe")  

#### Edit Recipe Page
If the user selects EDIT on the Manage Recipes page they are redirected to a page displaying the full recipe with their previous inputs pre-filling the various input fields. The user can change as few or as many field s as necessary or if they change their mind there is a option to Cancel the edit.  
![Recipe Edit](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/edit-recipe.png "Edit Recipe Wireframe")


#### Profile Page

#### Edit Profile Page
Enables the user to add a photo or avatar to their profile, provide their location and subscribe to the website.
I chose not to place the subscribe option on the landing page because until you log in you wouldn't necessarily know whether you wanted to subscribe to the website.
Thus it made sense to me to add this to a profile page

#### **Surface**


##### **Colour Scheme**


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
![Font](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/shrikhand.jpg) "Shrikhand" 

 - Page headings (Galada)  
For these I was looking for a more relaxed, fun font with a slightly cursive style and a bit of weight.  
![Font](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/galada.jpg) "Galada" 

 - Recipe Titles (Molle)  
I just had to use this font style! Something about it elicited a positive reaction with me and just seemed to work for the Recipe cards.  
![Font](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/molle.jpg) "Molle" 

 - Recipe Detail (Happy Monkey)  
Given the recipe notebook style I was trying to achieve I wanted a font which lokked more natural and 'written' than the typical online typography.  
![Font](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/happy-monkey.jpg) "Happy Monkey"

##### **Imagery** 

______

## **Features** <a name="features"></a>


### **Existing Features**

### **Security Reatures**

______

## **Technologies Used** <a name="technologies"></a>  

This website has been built using the following core technologies:

##### Core Coding languages

- ![HTML 5](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/html-5-logo.png "HTML5") - HTML5
- ![CSS3](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/css3-logo.png "CSS3") - CSS3
- ![Python](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/Python.png "Python") - Python
- ![Javascript](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/javascript.png "Javascript") - Javascript


##### Integrations

- ![Materialize CSS](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/materialize-css.png "Bootstrap 4") - Materialize CSS
- ![Font Awesome](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/fontawesome-logo.png "Font Awesome") - Font Awesome was the source of all icons.
- ![Google Fonts](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/googlefonts-logo.png "Google Fonts") - Fonts used on the website courtesy of Google Fonts
- ![JQuery](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/jquery.png "JQuery") - The project uses JQuery to simplify DOM manipulation.
- ![Flask](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/flask.png "Flask") - The project uses the Flask micro-framework and links with jinja to create the webpages
- ![Jinja](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/jinja.png "Jinja") - The project uses the Jinja templating engine
- PyMongo

#### Database Management System
- ![MongoDB Atlas](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/mongodb.png "MongoDB Atlas") - MongoDB Altas  
-![MongoDB Compass](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/mongodb.png "MongoDB Compass") - MondgoDB Compass was used to upload the JSON data to the W3Recipes Cluster  
- ![MongoDB Charts](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/mongodb.png "MongoDB Charts") - MongoDB Charts was used to create the website's dashboard

##### Version Control, storage and hosting

- ![Gitpod](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/gitpod-logo.png "Gitpod logo") - All of the website's code was written in the Gitpod IDE.
- ![Git](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/git-logo.png "git logo") - used for maintaining version control of the saved files.
- ![GitHub](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/github-logo.png "Github logo") - used as the primary repository for storying the files and documentation.
- ![Heroku](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/heroku-logo.png "Heroku logo") - Deployment site

##### Other

- Dillinger was once again used to edit the markdown required for the README file.
______

## **Testing** <a name="testing"></a>
All of the testing conducted on this app', and the bugs identified are documented in the following document:-
# [TESTING.md](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/TESTING.md) 

______
## **Database Creation** <a name="database"></a>
This app is connected to the MongoDB Atlas 
The following ste ps were used to create the data base and connect the 
 - Log in to MongoDB Atlas
 - Start a new Project

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
![Deployment]https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/heroku-github.jpg

 1. In the "Deployment Method" section select Github  
 Once selected a Connect to GitHub section will display below

![Deployment]https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/heroku-app-menu.jpg  

 2. Ensure your profile is displayed
    - If not type in your GitHub username
 3. Search for, and select the Repo corresponding to the Heroku app
 4. Click "Connect"

This app uses connec and Heroku requires these in order for the website to function as desired. To do this you need to set the Config Vars
 - Under the "Settings" tab, in the Config Vars section select the "Reveal Config Vars" button.
![Config Vars]https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/README-img/heroku-config-vars.jpg
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
   - Remembering to substitute in your own DBNAME and Password
 5. Copy your connection string

### **Enabling Automatic Deployment**
 - Select the Heroku "Deploy" tab
 - In the "Automatic deploys" section select the branch you wish to use
 
There is no difference between the developed version and that deployed on Heroku
______

## **Resources** <a name="resources"></a>

I have attempted to work independently as much as possible while building this website, choosing to solve my own issues, using web resources wherever possible. Thus, my main resource throughout this project was again the trusty Google search.
 Aside from Google I have made use of the following resources: -

- [Balsamiq](https://balsamiq.com/wireframes/) – Wireframing Tool
- Code Institute course material and Walkthrough projects
- Google DevTools - for trouble shooting and first pass testing
- Google Lighthouse - Website performance testing
- [StackOverFlow](https://stackoverflow.com/) – Web based coding tips
- [CSS Tricks](https://css-tricks.com/) – Styling tips like https://css-tricks.com/styling-underlines-web/
- [W3Schools](https://www.w3schools.com/) – General coding resource
- [MDN]("https://developer.mozilla.org/en-US/docs/Web/JavaScript") - Useful Javascript resource
- [Pexels](https://www.pexels.com/) – Licence free image repository
- [BeFunky](https://www.befunky.com/create/resize-image/) – Online image resizer
- [Color Picker](https://htmlcolorcodes.com/color-picker/) – HTML and CSS colour codes
- [W3C Validator](https://validator.w3.org/) - HTML and CSS Validation tool
- [JSHint](https://jshint.com/) - Javascript code analysis tool
- [JSLint](https://jslint.com/) - Javascript code quality analysis tool
- [SEO Site Checkup](https://seositecheckup.com/tools/custom-404-error-page-test) - Checks to see if you have a custom 404 page
- [Online Javascript Beautifier](https://codebeautify.org/jsviewer) - Useful tool for indenting JS code
- [Am I responsive?](http://ami.responsivedesign.is/) - provides a simple view of a websites responsiveness.

______

## **Credits** <a name="credits"></a>

### **Content**
The content of this website was created by Gareth John. Snippets of code have been taken from official documentation and sources creditted below and in the respective code files. All text was written 

### **Media**

The photos used in this site were obtained from the folloing sources:


- All other images came from my own personal image library

### **Code Snippets**
Much of the structure of this site follows what was taught during the Backend Development - Task Manager walkthrough project provided by Code Institute, but has been heavily modified to suit a recipe database site with additional functionality not provided in the walkthrough.

 | Feature | Description | Source |
 |:-------:|-------------|:------:|
 |Animated Arrows| Animated arrows in the Landing Page call to action.| https://freefrontend.com/css-arrows/#animated-arrows |

### **Acknowledgements** <a name="acknowledgements"></a>

- Thanks as always to everyone at the Code Institute for the excellent video tutorials and fantastic introduction to Python, Flask and some of the different databases structures. Tim Nelsons Walkthrough projects were particularly enjoyable.
 - Thanks to Ed Bradley for hosting a very helpfull MS3 Planning Call.
 - Thanks also to Can Sucullu for opening my eyes to potential vunerabilitis and potential back doors 
______
### **Technical Support** <a name="technical"></a>
If you encounter any issues with this website, or require any support please email the developer [johnge71@gmail.com](mailto:johnge71@gmail.com)