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
The following table explains the bugs and issues encountered while building this website.
|  Issue #   |  Bug or Issue  |  Description  |  Solution  |
|:----------:|:--------------:|---------------|------------|
| 001 |Page width exceeding viewport width|While conducting continuous testing I noticed the website was experienceing a sporadic issue with the page width increasing beyond the viewport width. Initially thought to affect all pages and caused by the moibile responsive navbar | While troubleshooting the issue I realised the problem was confined to my Recipes.html page, and thus couldn't be caused by the navber which is a consistent element on all pages. The only other interactive element on this page was an unused Materialize CSS "FeatureDiscovery" element. After deletion the Page width issue didn't reoccur
| 002 |Delete Confirmation in a modal|When a user selects delete on the "Manage Recipes" page I wanted a confirmation email to display before the recipe could be removed from the website and database. Initial attemps resulted in recipes being deleted one by one in a sequence since the modal was not linked to the specific recipe. This was verified using the {{ recipe title }} and by taking the chance and deleting one of the records | 
| 003 |Displaying Flash messages in a modal|  |  |
| 004 | Favicon 404 on some pages | My chosen Fav icon was not displaying on all pages which inherit from the base,html. The error code was "GET /full_recipe/static/img/favicon.ico HTTP/1.1" 404".| Adding a forward slash to the beginning of the directory address fixed the issue.
