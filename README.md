![W3 Recipes](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/document-title.jpg "Discover Kefalonia")

# [**W3 Recipes**](https://gazzaj.github.io/CI-MS2-Discover-Kefalonia/)


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

6. _As a _ **site owner**, _I need to_ **ensure security of information**, _in order to_ **prevent unauthorised editing or deletion of user uploaded data**.

7.  _As a _ **site owner**, _I need to_ **promote a product, _in order to_ **promote a preferred product on the site**.


### **The 5 Planes of UX** <a name="planes"></a>
The five planes provide a framework for discussing user experience.

#### **Strategy**  
The purpose of W3 Recipes website is to provide users with a convenient and easy means of searching, uploading and editting their favourite recipes. The aim is to try and upload  as many recipes from as many different countries as possible to provide a wide array of recipes, and as a bit of fun to track progress in this respect.

#### **Scope**  
Functionality is strictly limited until each user decides to register on the website, however once logged in users are able to:
 - **Create** or upload a recipe into the database which can then be viewed by all other registered users
 - **Read**, or view all of the recipes stored in the database.
    - The list of recipes can be filtered by country of origin
    - Search functionality enables the user to search the title and ingredient fields for keywords of their choice.
 - **Update** any of their own recipes, to change any of the previously stored content, or add additional information (within the limits of the input form)
 - **Delete** recipes they themselves have uploaded. This functionality is NOT extended to other users recipes.

Users will also be able to track which countries recipes have been uploaded for using the Dashboard page; and upvote recipes they like or have tried.

##### Functional Requirements
Simple and intuitive navbar with a clear mobile responsive equivalent.
Navbar selections which increases once a user registers or logs into the website
One page each to c

>A key consideration from early planning stages was the method for inputting the recipe ingredients and preparation steps. I had initially thought about getting the user to input the number of ingredients and then looping through this number to enter each ingredient, one at a time. However this would be problematic, if the user inputs an incorrect number. In this case they might have to restart the process, which would be undesirable. **Thus the goal; has been to make it as easy as possible for the user to input this data.**

##### Content Requirements
I am a keen cook, and having an image of a recipe is just as important as the ingredient list and preparation steps, as it provides an enticing view of the endpoint and helps to whet the users appetite. Thus including images with each recipe is a key component.
The typography selected for this site was also important, and needed to be fun yet functional. I have selected more cursive fonts to try and emulate a recipe notebook style.
I deliberately stuck with a cleand and simple structured layout to make it easy to view the content.

A consistent design is provided through Flask template inheritance




#### **Structure**  


##### Interaction Design


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
The landing page has no function other than to look enticing and to direct users to explore further.
The bulk of the website is incorporated on the main Explore/Discover page which houses the Google Map

![Landing Page](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/landing-page.png "Landing Page Wireframe")

##### Main Recipe Page
The Map page is the focal point for the website, combining interactive elements with Google map functionality. Clicking category buttons will drop Google Map markers on the Map; when each marker is clicked, information displays on the left-hand pane. This will include specific location image and information.

![Map Page](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/map-page.png "Map Page Wireframe")

>**_The main change here was to incorporate what could have comprised separate pages (About, Map and Gallery) into a single page._**

###### Individual Recipe Page

##### Dashbord Page


![Dashboard Page](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/contact-page.png "Contact Page Wireframe")

##### Registration Page

![Dashboard Page](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/contact-page.png "Contact Page Wireframe")

#### Login Page

![Dashboard Page](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/contact-page.png "Contact Page Wireframe")

#### Recipe Edit Page

![Recipe Edit](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/contact-page.png "Contact Page Wireframe")

#### Recipe Delete Page

![Recipe Delete](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/contact-page.png "Contact Page Wireframe")


#### **Surface**


##### **Colour Scheme**


##### **Typography**  
Selecting the correct typography for this site is just as important as the other design aspects. I want the fonts to reflect a more relaxed style, welcoming the user into the site.
 - Readable
 - Relaxed

I researched different styles which could be used for food related content:
 - https://www.creativebloq.com/inspiration/10-mouth-watering-restaurant-menu-fonts
 - https://line25.com/fonts/best-fonts-for-food-industry-design

I loaded various fonts into my CSS file and experimented with different combinations to find ones which compolemented each other and provided an asthetically pleasing look to the site.



##### **Imagery** 

______

## **Features** <a name="features"></a>


### **Existing Features**


______

## **Technologies Used** <a name="technologies"></a>  

This website has been built using the following core technologies:

##### Core Coding languages

- ![HTML 5](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/html-5-logo.png "HTML5") - HTML5
- ![CSS3](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/css3-logo.png "CSS3") - CSS3
- ![Javascript](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/javascript.png "Javascript") - Javascript
- ![Python](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/javascript.png "Javascript") - Python

##### Integrations

- ![Bootstrap 4](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/bootstrap-logo.png "Bootstrap 4") - Bootstrap 4
- ![Font Awesome](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/fontawesome-logo.png "Font Awesome") - Font Awesome was the source of all icons.
- ![Google Fonts](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/googlefonts-logo.png "Google Fonts") - Fonts used on the website courtesy of Google Fonts
- ![JQuery](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/jquery.png "JQuery") - The project uses JQuery to simplify DOM manipulation.


##### Version Control, storage and hosting

- ![Gitpod](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/gitpod-logo.png "Gitpod logo") - All of the website's code was written in the Gitpod IDE.
- ![Git](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/git-logo.png "git logo") - used for maintaining version control of the saved files.
- ![GitHub](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/github-logo.png "Github logo") - used as the primary repository for storying the files and documentation.
- - ![Heroku](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/github-logo.png "Heroku logo") - Deployment site

##### Other

- Dillinger was once again used to edit the markdown required for the README file.
______

## **Testing** <a name="testing"></a>

### **User Story Testing** <a name="user-story-testing"></a>
The following testing has been carried out to validate how the website addresses each of the user stories:
|User Story|Desctiption|Testing|
|:--------:|-----------|-------|
|1|As a , I need to , in order to . ||

![Landing Page](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/landing-page.jpg "Landing Page View")
![Map Page](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/map-page.jpg "Map Page View")


|User Story|Desctiption|Testing|
|:--------:|-----------|-------|
|2|As a , I need to , in order to .||

![Weather Info](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/weather-info.jpg "Weather Info View")
![Beach Info](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/poi-info.jpg "Beach Info View")
![User Feedback](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/ecuser-comment.jpg "Weather User Feedback")


|User Story|Desctiption|Testing|
|:--------:|-----------|-------|
|3|As a user, , in order to ||

![Town Info](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/town-info.jpg "Town Info View")
![User Feedback](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/ftuser-comment.png "POI User Feedback")

|User Story|Desctiption|Testing|
|:--------:|-----------|-------|
|4|As a , I need to , in order to ||

![Activity Info](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/activity-info.jpg "Activity Info View")
![User Feedback](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/kmuser-comment.jpg "Activity user feedback")

|User Story|Desctiption|Testing|
|:--------:|-----------|-------|
|5|As a , , in order to ||

![Contact Page](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/contact-form.jpg "Contact Page view")

### **Functionality Testing** <a name="functionality-testing"></a>
The following table captures the functional testing performed on the website to ensure it works as desired. I have tested on the listed browsers only using Windows version 1909 (OS Build 18363.1256), and have not conducted any backward compatibility testing in older browser versions.

|   Test       |Purpose          | Desired Result | Actual Result | Chrome v 87.0.4280.88 | Firefox v 83.0 (64-bit) |
|:------------:|-----------------|----------------|---------------|:------:|:-------:|
|   001        | Test Navigation | |  |  |  |
|   002        | Test Navigation | |  |  |  |
|   003        | Test Navigation | |  |  |  |
|   004        | Test Navigation | |  |  |  |
|   005        | Test Navigation | |  |  |  |
|   006        |   | |  |  |  |
|   007        |   | |  |  |  |
|   008        |   | |  |  |  |
|   009        |   | |  |  |  |
|   010        |   | |  |  |  |
|   011        |   | |  |  |  |
|   012        |   | |  |  |  |
|   013        |   | |  |  |  |
|   014        |   | |  |  |  |
|   015        |   | |  |  |  |
|   016        |   | |  |  |  |
|   017        |   | |  |  |  |
| 018          |   | |  |  |  |
| 019          |   | |  |  |  |
|020           |   | |  |  |  |
| 021          |   | |  |  |  |
| 022          |   | |  |  |  |
|023           |   | |  |  |  |

The philosophy I have used throughout this build is to code, review and test each part of the website as I progressed, relying heavily on Google Dev tools throughout, for first pass testing.

### **Code Quality and Validation** <a name="code-validation"></a> 
|Test|Process|Result| Comment |
|----|-------|:----:|---------|
|HTML Validation| Copy Index.html code into W3C validator|PASS||
|HTML Validation| Copy Map.html code into W3C validator|PASS||
|HTML Validation| Copy Contact.html code into W3C validator|WARNING|The "type" is unnecessary for Javascript results from 3rd party Script tags|
|HTML Validation| Copy 404.html code into W3C validator|PASS||
|Javascript Validation| Copy index.js code into JSHint|CHECKED||
|Javascript Validation| Copy map.js code into JSHint|CHECKED||
|Javascript Validation| Copy cndex.js code into JSHint|CHECKED||
|CSS Validation| Copy CSS code into WC3 validator| ERROR |Errors raised for webkit compatibility. Chosen to ignore| 
|Python Validation|Copy Python code into |||

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
I have conducted continuous responsiveness testing, right up to the final submission, to ensure the website functions on different devices and in both portrait and landscape orientation, using:
 - Google Devtools
![Responsiveness](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/poi-info.jpg "Website Responsiveness") 
![Responsiveness](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/contact-form.jpg "Website Responsiveness")
 - Am I Responsive
![Am I responsive images](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/am-i-responsive.png "Am I Responsive")
 - Responsinator.com
 ![Responsinator image](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/responsinator.png "Responsinator image")

### **Performance Testing** <a name="performance-testing"></a>
The website has been performance testing using the following tools:
 - Google Lighthouse (Desktop)
  
 
![Google Lighthouse](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/google-lighthouse.png "Google Lighthouse Testing")



 - Google Lighthouse (Mobile)
  
 
![Google Lighthouse](https://github.com/GazzaJ/CI-MS2-Discover-Kefalonia/blob/master/readme-img/google-lighthouse-mobile.png "Google Lighthouse Testing")


______

## **Bugs and Issues** <a name="bugs"></a>
|  Issue #   |  Bug or Issue  |  Description  |  Solution  |
|:----------:|:--------------:|---------------|------------|
| 001 |Flash Messages displayed in a modal|While conducting continuous testing I noticed the website was experienceing a sporadic issue with the page width increasing beyond the viewport width. Initially thought to affect all pages and caused by the moibile responsive navbar | While troubleshooting the issue I realised the problem was confined to my Recipes.html page, and thus couldn't be caused by the navber which is a consistent element on all pages. The only other interactive element on this page was an unused Materialize CSS "FeatureDiscovery" element. After deletion the Page width issue didn't reoccur
| 002 |Delete Confirmation in a modal|When a user selects delete on the "Manage Recipes" page I wanted a confirmation email to display before the recipe could be removed from the website and database. Initial attemps resulted in recipes being deleted one by one in a sequence since the modal was not linked to the specific recipe

 

 - Page Width Issue

 I conducted some troubleshooting to investigate the problem.
>.
______

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
- Insert your app name
  - Heroku will let you know whether your chosen name is available
- Select the most appropriate region for your location
- Click the "Create app" button

### **Heroku Deployment**
The above steps will automatically bring you to the "Deploy" tab of your new app
 1. In the "Deployment Method" section select Github
 Once selected a Connect to GitHub section will display below
 2. Ensure your profile is displayed
    - If not type in your GitHub username
 3. Search for, and select the Repo corresponding to the Heroku app
 4. Click "Connect"

This app uses connec and Heroku requires these in order for the website to function as desired. To do this you need to set the Config Vars
 - Under the "Settings" tab, in the Config Vars section select the "Reveal Config Vars" button
This will reveal a form for inputting the key and value pairs necessary to connect to the app. The

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
The content of this website was created by Gareth John. Snippets of code have been taken from official documentation and sources creditted below and in the respective code files. All text was written  by the developer having researched the island. Image credits are provided in the following section.

### **Media**

The photos used in this site were obtained from the folloing sources:


- All other images came from my own personal image library

### **Code Snippets**
The code I use to deploy and clear the Google maps markers has been adapted from the Google Maps API Developer documentation 

### **Acknowledgements** <a name="acknowledgements"></a>


- Thanks as always to everyone at the Code Institute for the excellent video tutorials and fantastic introduction to Javascript, Jasmine and RESTful API's.

______
### **Technical Support** <a name="technical"></a>
If you encounter any issues with this website, or require any support please email the developer [johnge71@gmail.com](mailto:johnge71@gmail.com)