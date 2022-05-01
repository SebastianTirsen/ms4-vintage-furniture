# Vintage Furniture online store

The Vintage Furniture online store is the best place to shop for the furniture and lighting connoisseur. Here you can find used furniture and lamps from famous designers and brands. The furnitures condition range from worn to like new and the prices are well below the ordinary price for a brand new piece. Teh store often has a wide variety of furniture and lightings and offer a great delivery service free of charge for orders just over 1000 SEK. If you cant find the piece of furniture or lighting that you want to buy at the moment, or you have another question, feel free to contact us by sending us a message via our Support form at the top of the first page. If you make a purchase with us, we would be delighted if you would leave us a review in the ratings section at the top of the frontpage, telling us what you think about your buying experience with us. View the live Website [here](https://ms4-vintage-furniture.herokuapp.com/).


![Mockup](readme-images/mockup-vf.png)

## Table of Contents
* [User Experience Design (UX)](#User-Experience-Design)
    * [The Strategy Plane](#The-Strategy-Plane)
        * [Site Goals](#Site-Goals)
        * [User stories](#User-Stories)
    * [The Scope Plane](#The-Scope-Plane)
    * [The Structure Plane](#The-Structure-Plane)
    * [The Skeleton Plane](#The-Skeleton-Plane)
        * [Wireframes](#Wireframes)
        * [Database Design](#Database-Design)
        * [Security](#Security)
    * [The Surface Plane](#The-Surface-Plane)
        * [Design](#Design)
            * [Colour Scheme](#Colour-Scheme)
            * [Typography](#Typography)
            * [Imagery](#Imagery)
- [Features](#Features)
    * [Existing Features](#Existing-Features)
    * [Features to be added](#Features-Left-to-add)
* [Technologies](#Technologies)
* [Testing](#Testing)
    * [Test Strategy](#Test-Strategy)
    * [Test Results](#Test-Results)
    * [Issues and Resolutions](#Issues-and-Resolutions-to-issues-found-during-testing)
* [Deployment](#Deployment)
    * [Project Creation](#Project-Creation)
    * [GitHub Pages](#Deployment-To-Heroku)
    * [Run Locally](#Run-Locally)
    * [Fork Project](#Fork-Project)
* [Credits](#Credits)
  * [Content](#Content)
  * [Acknowledgements](#Acknowledgements)

****

## User Experience Design
### **The Strategy Plane**

The interior design industry has boomed in the latest years and home-styling is now a household concept. 
The spending on furniture and lighting with high quality and design has increased exponentially. Vintage 
Furniture is the answer to this demand, but offers furniture that are slightly used and at significantly lower
prices to the cost conscious interior design connoisseur.

The goal of this Website is to provide consumers with the opportunity to make purchases of designer furniture and lightning at lower cost. The Vintage Furniture Online store offers second hand, high quality furniture made by famous designers and brands. The users are provided with a simple and easy to use website that allows them to find a piece of furniture or lighting to buy at a significantly lower price than if purchased new in some other store.

#### Site Goals
* Help the users find used furniture from famous designers and brands to buy at lower prices, all in one place.
* Inform the users about the furnitures and lightings by providing a easy-to-use website with fast access to the most 
important details about different furnitures and lightings.
* Offer users an easy buying experience with fast and secure checkout with card-payment.
* Provide users with the opportunity to save their information for an easy buying experience next time they shop at the site.
* Inform the users of what other customers think about the site and their pruchasing experience, by giving the users the possibility to rate the site.

#### User stories
* As a user, I want the main purpose of the site to be clear so that I immediately know what the site is intended for upon entering.
* As a user, I want to easily navigate the site so that I can find content quickly with ease.
* as a user I want to be able to view the furniture and lighting in different categories to quickly find what I am looking to buy.
* as a user I want fast and easy access to information on specific furniture and lighting to facilitate my purchase decision.
* As a user, I want to quickly search the entire store for a furniture or lighting to buy.
* As a user, I want the website to be responsive so that I can clearly view the webpages from my mobile, tablet or desktop.
* As a user, I want to be able to register to the website so that I can have an easy buying experience and save information on my orders.
* As a user, I want a way to contact the site owner so that I can have any questions I may have in regards to the website answered.
* As a user, I want to get information about other customers opinions about the store and to inform other customers of my opinion of the store.
* As a user I want a fast, easy to use and secure checkout and payment.
* as a store owner I want a way of communicating with clients that have questions about the site and their purchases.
* as a store owner I want a way to manage furniture that are to be sold on the site. I want to be able to add new furniture, delete furniture and edit furniture that have information saved that for some reason needs to be changed.

### **The Scope Plane**

**Features planned:**
* Responsive design.
* Website title, a dominant logo and information on the site purpose.
* A clear navigation Menu.
* Postgres default and fallback Sqlite databases to store information.
* CRUD Functionality so that the store owner can manage the furnitures.
* Login functionality.
* Logout functionality.
* Profile Page for the users stored info and past orders.
* All the furnitures and Lighting displayed on one page.
* All the details on the individual furnitures and Lighting displayed on separate pages.
* Display of all the users posted ratings and reviews.
* Registered user creation and management of their own ratings.
* Fast and secure checkout and payment with Stripe.

### **The Structure Plane**
User Story:
> As a user, I want the main purpose of the site to be clear so that I immediately know what the site is 
intended for upon entering.

Acceptance Criteria:
* Site Logo to be displayed on the main navigation bar on all pages and across all devices.
* Home Page to display Website Title and information to the user on the purpose of the site.
* Pictures and text displayed of new furnitures that have come in to the store.

Implementation:

A site logo will be displayed on the main navigation menu. This should be 
displayed on all webpages.

The Website title will be displayed on the home page and a description of the 
site will be displayed on the Home page so that is evident of the websites
purpose as soon as the user visits the site.

User Story:
> As a user, I want to be able to easily navigate the site so that I can find content quickly and with ease.

Acceptance Criteria:
* Navigation menu to be displayed on all pages.
* All navigation links redirect to the correct pages.
* the navigations are made respponsive to fit all types of devices.

Implementation:
A two part navigation menu will be displayed on all webpages. A top navigation concerning the users and 
their purchases and a main navigation concerning th furnitures and lightings. This will redirect users to 
the approriate page when clicked. On smaller devices, the menu will collapse into a hamburger menu to make efficient
use to screen space. When clicked, the menu will expand downward on the screen displaying all navigation items.

The following navigation items will be implemented:

visible to all users:
* Search-field
Top navigation:
* My account - Register
             - Log In
* Shopping Dolly
* Support
* Rate Us

Main navigation:
* All Furniture - By price
                - By Brand
                - By Category
* Furniture - Tables
            - Chairs
            - Storage
            - Shelves
            - all furniture
* Lighting  - Ceiling & Wall lights
            - Desk lamps
            - Floor lamps
            - all lighting
* Special offers - New arrivals
                 - Deals
                 - Clearance
                 - all specials

visible only to logged in users:
* My account - profile
             - Log out
* Edit and Delete-buttons on ratings page.

visible only to logged in superusers/store owners:
* My account - Furniture Management
* Edit and delete links on the all furniture page
and on furniture details page.

User Story:
> as a user I want to view the furniture and lighting in different categories to quickly find what I am looking to buy.

Acceptance Criteria:
* The user should be able to sort the furniture and lightings by different variables such as price, brand and category. 
* The user needs to be able to view only categories of their choice.

Implementation:
Under the "All furnitures" button in the navigation, the options are available to sort the furnitures by price,
brand and category. Under the buttons "Furniture", "Lighting" and "Specials" there are different categories to choose.
When the user selects a category, only the furnitures in that category becomes visible to the user.

User Story:
> as a user I want fast and easy access to information on specific furniture and lighting to facilitate my purcchase decision.

Acceptance Criteria:
* The user should be able to have direct access to the details of the individual furnitures just by clicking once.
* The user should be able to exit the individual furnitures just by clicking once and view all the furnitures again.

Implementation:
If the user is interested in more information about a certain piece of furniture, they click on the image
to get to a page showing the specific details of the selected item. When the user is satisfied, they click the button
named "Keep shopping" to view all the furnitures again.

User Story:
> As a user, I want to quickly search the entire store for a furniture or lighting to buy.

Acceptance Criteria:
* A searchfield should be visible to the user and make it possible to search th whole site for an item by typing in a word and clicking search-button.

Implementation:
A searchfield is placed at the center of the navigation and is visible on all pages on the site. The user can search on every page by typing
in a word and hitting the search-button. 

User Story:
> As a user, I want the website to be responsive so that I can clearly view the webpages from my mobile, 
tablet or desktop.

Acceptance Criteria:
* Content should be responsive and display clearly on all devices.

Implementation:
Bootstrap and templates will be used for website layout with suitable column sizes and containers to ensure
that all content is displayed clearly on all devices. Images will be responsive and 
scale to fit screen sizes with no stretch or distortion to ensure clear images are displayed to the user.

User Story:
> As a user, I want to be able to register to the website so that I can have easy access to my buyer
information and previous orders.

Acceptance Criteria:
* Register - Functionality to register a new user profile to be added.
* Log in/out - Login and Logout functionality to be added.
* Profile page - User must be able to display their basic details and previous orders.
* Profile page - User must be able to edit their basic details.
* User must have the ability to post, update and delete ratings made by themselves.
* Only the store owner should have the ability to update or delete the furnitures.

Implementation:
A Register page will be implemented that allows users to register for an account on the website. The username
and the password along with email for the users account will be stored in Postgress collection called users.

A Log In page will be implemented to allow registered users the ability to login in to their account. Once a user has successfully logged in, 
they will be redirected to the Homepage. A message will be displayed to inform the user that they have successfully logedd in. In the navigation 
under "My account" the logged in user can find the Profile page "My profile". The users Profile page will display the basic details, along with 
the users previous orders. The user will be able to click on the individual previous orders to view details of the order. The basic information 
about the user can also be modified by the logged in user. The purpose is to make it possible for the user to change address and shipping information.

A Log Out link will be displayed to users who are logged in. When clicked this will redirect the user to a page where they are asked if they are sure
that they want to log out. Under the question there are two buttons, one for cancelling the logout and one for signing the user out. When the user chooses to log out the user are redirected to the Home page. A message will be displayed to inform the user that they have successfully logedd out. If they cancel their log out, they are redirected to the homepage.

User Story:
> as a store owner I want to manage furnitures that are to be sold on the site.

Acceptance Criteria:
* Add new furniture. 
* Delete furniture.
* Edit furniture.

Implementation:
In order to be able to add a new furniture, modify or delete an existing furniture, a user will have to be a store owner
and registered as a superuser. The management of furnitures to be sold are maintained on the "Furniture management" page
found in the dropdown "My account" in the navigation. Only the store owner will have the ability to update or delete the furnitures 
for sale, this is to prevent unwanted modification or deletion of items for sale by the common user. The store owner are able to edit 
all the information about the furnitures on the management page. A message will be shown tothe superuser to alert them whether the 
update or delete on the furniture was successful. 

User Story:
> As a user, I want a way to contact the site owner so that I can have any questions I may have in regards to the website answered.

Acceptance Criteria:
* Support page should be added with a contact form.

Implementation:
A support page will be added that contains a template with text inputs, this will allow users to contact the site 
owner. The information is stored in the Postgress collection called supports. A  message is displayed to alert 
the user that the support message was sent successfully.

User Story:
> As a user, I want read other customers opinions about the store and to inform other customers of my opinion of the store.

Acceptance Criteria:
* All posted ratings must be displayed to all users.
* Users should be able to read all the reviews and ratings.
* Users that are logged in should be able to give a rating and write a review and save it for others to read.
* Users that are logged in should be able to edit their own posted ratings.
* Users that are logged in should be able to delete their own posted ratings.

Implementation:
A "Rate Us" page will be acessible on the navigation menu visible to all users. The page will display all the ratings
and reviews made by all users. The ratings page will display a button for adding a new rating and review text.
All the ratings made by all users will be displayed on the page. Two buttons will be visible to the side of the ratings 
made py the logged in user, for deleting and editing their own rating. The ratings and reviews information will be stored
in a Postgress database collection called ratings.

User Story:
> As a user I want a fast, easy to use and secure checkout and payment.

Acceptance Criteria:
* a summary of all the items i want to buy.
* A easy to use checkout process.
* A secure confirmation that the order has been registered.

Implementation:
The shopping dolly page gives the users an easy way to get a summary of all the furniture that they want to order.
The checokut process are easy and made secure by using Stripe payments by card nymber input.
When the user clicks the button to complete the order a message shows to confirm that the order was successfully processed.
The order is assigned a unique order number that is visible in the confiormation message. A confirmation email will be sent 
to the users registered email. A confirmation page is also shown with all the information regarding the order displayed.

### **The Skeleton Plane**
#### Wireframes

Homepage:<br>
![Homepage](readme-images/wire-homepage.png)<br>
All Furnitures:<br>
![All Furnitures](readme-images/wire-all-furnitures.png)<br>
Furniture:<br>
![Furniture](readme-images/wire-furniture.png)<br>
Profile:<br>
![Profile](readme-images/wire-account.png)<br>
Dolly:<br>
![Dolly](readme-images/wire-bag.png)<br>
Support:<br>
![Support](readme-images/wire-support.png)<br>
Rating:<br>
![Rating](readme-images/wire-rating.png)<br>
Checkout:<br>
![Checkout](readme-images/wire-checkout.png)<br>
Management:<br>
![Management](readme-images/wire-management.png)<br>
Signup:<br>
![Signup](readme-images/wire-signup.png)<br>
Login:<br>
![Login](readme-images/wire-login.png)<br>

#### Database Design
Postgress Databas structure:

**Collection: contacts**<br>
{<br>
&nbsp;&nbsp;&nbsp;&nbsp;_id: unique-value,<br>
&nbsp;&nbsp;&nbsp;&nbsp;name: "Sebastian Tirsén"<br>
&nbsp;&nbsp;&nbsp;&nbsp;email: "sebastian.tirsen@gmail.com"<br>
&nbsp;&nbsp;&nbsp;&nbsp;message: "I really like your site man!"<br>
}

**Collection: ratings**<br>
{<br>
&nbsp;&nbsp;&nbsp;&nbsp;_id: unique-value,<br>
&nbsp;&nbsp;&nbsp;&nbsp;rating: "5",<br>
&nbsp;&nbsp;&nbsp;&nbsp;review: "Best show of all times!",<br>
&nbsp;&nbsp;&nbsp;&nbsp;created_by: "sebbe",<br>
&nbsp;&nbsp;&nbsp;&nbsp;show: "Game of Thrones",<br>
}

**Collection: series**<br>
{<br>
&nbsp;&nbsp;&nbsp;&nbsp;_id: unique-value,<br>
&nbsp;&nbsp;&nbsp;&nbsp;country: "France",<br>
&nbsp;&nbsp;&nbsp;&nbsp;director: "James Cooper",<br>
&nbsp;&nbsp;&nbsp;&nbsp;genre: "Comedy",<br>
&nbsp;&nbsp;&nbsp;&nbsp;parental_guidance: "+18 years",<br>
&nbsp;&nbsp;&nbsp;&nbsp;picture: "picture link",<br>
&nbsp;&nbsp;&nbsp;&nbsp;seasons: "12",<br>
&nbsp;&nbsp;&nbsp;&nbsp;starring: "Nils Lofgren",<br>
&nbsp;&nbsp;&nbsp;&nbsp;synopsis: "When chemistry teacher Walter White is diagnosed with...",<br>
&nbsp;&nbsp;&nbsp;&nbsp;title: "Smelling Bad",<br>
&nbsp;&nbsp;&nbsp;&nbsp;year: "2011",<br>
&nbsp;&nbsp;&nbsp;&nbsp;posted_by: "sebbe",<br>
}

**Collection: users**<br>
{<br>
&nbsp;&nbsp;&nbsp;&nbsp;_id: unique-value,<br>
&nbsp;&nbsp;&nbsp;&nbsp;name: "Sebastian",<br>
&nbsp;&nbsp;&nbsp;&nbsp;email: "sebastian.tirsen@gmail.com",<br>
&nbsp;&nbsp;&nbsp;&nbsp;username: "sebbe",<br>
&nbsp;&nbsp;&nbsp;&nbsp;password: hashed-value,<br>
}

#### Security

Database connection details are set up in an [env.py](https://pypi.org/project/env.py/) for development, for 
security reasons this is not uploaded to GitHub so that database and connection details are not visible to 
users. In production these are stored in Heroku. 


### **The Surface Plane**
### Design

#### Colour Scheme
The main background colour is plain white ![#fff] for the body

The footers background color i adopted from the  Material Design Boostrap Footer Template, which are light grey ![#f8f9fa] and black with low opacity rgba(0, 0, 0, 0.05).

All the buttons backgrounds and border color are from the standard Bootstrap class btn-primary, which is blue ![#0d6efd]. 

The main website text is black ![#000000] and the footer text is ![#6c757d].

Several other colors have also been used on small objects on the site.

#### Typography

Plain text is font-family: 'Poppins', sans-serif;.

Headings are font-family: 'Open Sans','Helvetica Neue',Helvetica,Arial,sans-serif;.

#### Imagery
A background is used on all pages displaying the character Ned Stark, from the show "Game of Thrones", sitting on "the iron throne". This image was 
taken from [The New Daily](https://1v1d1e1lmiki1lgcvx32p49h8fe-wpengine.netdna-ssl.com/wp-content/uploads/2016/06/ned-stark-game-of-thrones-740x385.jpg). 

The website logo was created only using the the initials of the name "(I)nternational (S)eries (D)ata(b)ase in plain white text.

Other Images can vary depending on what pictures are stored on the show cards in the database.

****
## Features

### Existing Features

* Home page displaying images and information on the sites purpose.
* User sign up functionality.
* Log in / Log out functionality.
* Event page that displays the next six events from todays date and allows users to search for events.
* Post New Show page allowing logged in users to post a new show.
* Profile page showing user information and shows posted by the user with update and delete functionality.
* Contact page with form connected to database contact Collection.
* Mobile responsive design.
* Site wide footer containing contact information, social media links, Copyright info and useful Site Links to streaming services.

### Features to be added

A feature to be included in a new release would be a searchfield. This would give the users a faster way to find a show in the Db especially when the amount of shows grow.

Filter and sort buttons would also make it easier for the user to navigate between different shows based on preference.

Each show having its own rank based on the average rating of the users, would be a great feature. Teh the user would have the possibility to filter all the shows based on any of the bits of information, for example "genre", and then sort them by ranking, finding the highest rated show in that genre. 

****
## Technologies

* [jinja](https://jinja.palletsprojects.com/en/3.0.x/)
    * This project uses Jinja templating language to minimize the duplication.
* [HTML](https://en.wikipedia.org/wiki/HTML)
	* This project uses HTML as the main language used to complete the structure of the Website.
* [CSS](https://en.wikipedia.org/wiki/CSS)
	* This project uses custom written CSS to style the Website.
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
    * JavaScript is used along with [emailjs](https://www.emailjs.com/) for the contact form. This sends an email to the owner
    on form submit.
    * [jQuery](https://jquery.com/) is used for the following: 
        * Mobile side nav
        * Displaying Success/Fail message verifying contact form status.
        * Collapsible Materialize elements.
        * Materialize modal.
        * Datepicker functionality on forms.
        * To populate downdrops on select elements.
* [Python](https://www.python.org/)
    * This projects core was created using Python, the back-end logic and the means to run/view the Website.
    * Python Modules used these dependencies listed in the requirements.txt file:
        * asgiref==3.5.0
        * boto3==1.22.4
        * botocore==1.25.4
        * dj-database-url==0.5.0
        * Django==3.2
        * django-allauth==0.41.0
        * django-countries==7.2.1
        * django-crispy-forms==1.14.0
        * django-storages==1.12.3
        * gunicorn==20.1.0
        * jmespath==1.0.0
        * oauthlib==3.2.0
        * Pillow==9.1.0
        * psycopg2-binary==2.9.3
        * python3-openid==3.2.0
        * pytz==2022.1
        * requests-oauthlib==1.3.1
        * s3transfer==0.5.2
        * sqlparse==0.4.2
        * stripe==2.74.0


* [MongoDB](https://www.mongodb.com/1)
    * MongoDB was used to create the document based databases(collections) used as data storage for this project.
* [Google Fonts](https://fonts.google.com/)
	* Google fonts are used throughout the project to import the *Inter* and *Bevan* fonts.
* [GitHub](https://github.com/)
	* GithHub is the hosting site used to store the source code for the Website.
* [Git](https://git-scm.com/)
	* Git is used as version control software to commit and push code to the GitHub repository where the source code is stored.
* [Heroku](https://dashboard.heroku.com/apps)
    * Heroku was used to deploy the live website.
* [Google Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools)
	* Google chromes built in developer tools are used to inspect page elements and help debug issues with the site layout and test different CSS styles.
* [Adobe XD](https://www.adobe.com/se/products/xd.html)
	* This was used to create wireframes.
* [Font Awesome](https://fontawesome.com/)
    * All the Icons displayed throughout the website are Font Awesome icons.
* [Favicon](https://favicon.io/)
    * Favicon.io was used to make the site favicon 
* [Techsini](http://techsini.com/multi-mockup/index.php)
    * Multi Device Website Mockup Generator was used to create the Mock up image in this README
* [Autoprefixer CSS Online](https://autoprefixer.github.io/)
    * Autoprefixer was used to parse my CSS and add vendor prefixes.

****
## Testing

### Test Strategy
#### **Summary**
Testing is required on all features and user stories documented in this README. 
All clickable links are tested and redirects to the correct pages. All forms linked to MongoDB
is tested to ensure they insert all given fields into the correct collections.

### Responsiveness

All pages were tested to ensure responsiveness on screen sizes from 390px and upwards on Chrome, Safari and Firefox browsers.

Steps to test:

1. Open browser and navigate to [Vintage Furniture](https://ms4-vintage-furniture.herokuapp.com/)
2. Open the developer tools (right click and inspect)
3. Set to responsive and decrease width to 390px
4. Set the zoom to 50%
5. Click and drag the responsive window to maximum width

Expected:

Website is responsive on all screen sizes and no images are pixelated or stretched.
No horizontal scroll is present.
No elements overlap.

Actual:

Website behaved as expected down to width 390px. However some minimal horisontal scroll seems to be present.

Website was also opened on the following devices and no responsive issues were seen:

- Ipad Air
- Iphone 12 Pro
- Ipad Mini
- Samsung Galaxy S20 Ultra

### Accessibility

Manual tests were performed to ensure the website was accessible as possible and to identify accessibility issues.

Testing was focused to ensure the following criteria were met:

- All links easily accessible and working, and sending the user to the right page and in a logical order
- Color contrasts sufficient.
- Heading levels are not missed or skipped, if not motivated by context, to ensure the importance of content is relayed correctly to the end user
- All content is contained within landmarks to ensure ease of use for assistive technology, allowing the user to navigate by page regions
- HTML page lang attribute has been set
- Aria properties have been implemented correctly
- All the features working correctly.

## Performance

The site performance was tested using Lighthouse in the developer tool in Chrome.

The performance for mobile use was scored as: 

Performance 67 Accessibility 86 Best Practices 92 SEO 83

The performance for desktop use was scored as:

Performance 91 Accessibility 79 Best Practices 92 SEO 80

Most important issues to improve Performance was to send pictures in more modern formats than jpeg or png.


**Navigation Links**

Testing was performed to ensure all navigation links on the respective pages, navigated to the correct pages as per design. This was done by clicking on the navigation links on each page.

| Navigation Link | Page to Load    |
| --------------- | --------------- |
| Icon-link       | index.html      |
| Home            | index.html      |
| Login           | login.html      |
| Register        | register.html   |
| Contact         | contact.html    |
| Your Profile    | profile.html    |
| All Shows       | cards.html      |
| New Show        | post_show.html  |
| Log Out         | login.html      |

Links on all pages navigated to the correct pages as exptected.

**Form Testing**

The form on the home page was tested to ensure it functioned as expected when correct data was input and when incorrect data was input. The following test scenarios were covered:

_Scenario One - Correct Inputs_

Steps to test:

1. Navigate to [Vintage Furniture](https://ms4-vintage-furniture.herokuapp.com/accounts/login/)
2. Scroll down to the form and input the following data:
   - Username: Sebbe
   - Password: Gabbeluba
3. Click Log In
4. User should be redirected to the Homepage.

Expected:

Form submits with no warnings or errors and user is redirected to the logged in users profile.html page. Successmessage is displayed
that user successfully signed in as <username>.

Actual:

Website behaved as expected with no errors or warnings and redirected to Homepage.

_Scenario Two - Correct Inputs_

Steps to test:

1. Navigate to [Vintage Furniture](https://ms4-vintage-furniture.herokuapp.com/profile/)
2. Scroll down the form.
3. Change info in one or more input fields.
4. Press update button.
5. User redirects to Profile page and success message informs about Profile Updated Successfully.

Expected:

Form submits with no warnings or errors and user is redirected to the Profile page and success message informs user about success of update.

Actual:

Website behaved as expected with no errors or warnings and redirected to Profile page.

_Scenario Three - Correct Inputs_

Steps to test:

1. Navigate to [Vintage Funriture](https://ms4-vintage-furniture.herokuapp.com/rating)
2. Press Add Rating button.
4. Modal appears asking user to type name and message.
5. Type in name and message in designated fields.
6. Press "Add" button.
7. User redirects to Ratings page and the new posted rating is posted and visible.
8. Press "Delete" button beside the new post.
9. Modals becomes visible asking if you are sure about deleting the rating.
10. Press "Delete" button in modal.
11. User is redirected back to ratings page and the deleted rating is no longer visible.

Expected:

Show is deleted with no warnings or errors and user is redirected to the ratings page and flash message informs user about success of 
deletion.

Actual:

Website behaved as expected with no errors or warnings and redirected to ratings page.


_Scenario Four - Correct Inputs_

Steps to test:

1. Navigate to [ISDb](http://ms3-seriesdb-project.herokuapp.com/cards)
2. Scroll down to the form and select a posted show a show:
   - Press Rate Show button.
   - modal is displayed asking for user to Rate show by clicking desired amount of star and writing a short review.
3. Press Save Rating button.
4. User redirects to cards.html and flash message informs about Rating Successful.
5. Press Review heading to display accordion info, check if the posted rating is displayed.

Expected:

Rating is posted with no warnings or errors and user is redirected to the cards.html page and flash message informs user about success of 
rating.

Actual:

Website behaved as expected with no errors or warnings and redirected to cards.html.


_Scenario Five - Correct Inputs_

Steps to test:

1. Navigate to [ISDb](http://ms3-seriesdb-project.herokuapp.com/post_show)
2. Fill in the information about the show:
   - Choose info in dropdowns.
   - fill in info in textfields.
   - paste in a correct link for the Picture Link.
3. Press Post Show button.
4. Navigate to profile page to find the posted show.

Expected:

Show is posted with no warnings or errors and user is redirected to the post_show.html page and flash message informs user about success of 
Post.

Actual:

Website behaved as expected with no errors or warnings and redirected to post_show.html.


_Scenario Six - Correct Inputs_

Steps to test:

1. Navigate to [ISDb](http://ms3-seriesdb-project.herokuapp.com/post_show)
2. Fill in the information about the show:
   - Choose info in dropdowns.
   - fill in info in textfields.
   - paste in a correct link for the Picture Link.
3. Press Post Show button.
4. Navigate to profile page to find the posted show.

Expected:

Show is posted with no warnings or errors and user is redirected to the post_show.html page and flash message informs user about success of 
Post.

Actual:

Website behaved as expected with no errors or warnings and redirected to post_show.html.


**Footer Social Media Icons / Links**

Testing was performed on the Font Awesome Social Media icons in the footer to ensure that each one opened in a new tab.

Each item opened a new tab when clicked as expected.

**Footer Quick Links**

Testing was performed on the links in the Quick Links section of the footer to ensure behaviour was as expected.

Each link redirected to the correct page when clicked as expected.


### Validator Testing 


HTML Code passed through the with no errors [W3C HTML Validator](https://validator.w3.org/#validate_by_input).

CSS Code passed through the with no errors [W3C CSS Validator](https://jigsaw.w3.org/css-validator/).

JavaScript code passed through the with no errors[JSHint Validator](https://jshint.com/).

Python Code passed through with no errors[PEP8 Validator](http://pep8online.com/).


#### **Access Requirements**
For testing the site, just register a new user and then login.

In order to manually verify the insertion of records to the 
collections, the tester must have access to MongoDB.

#### **Regression Testing**
All features previous tested during development in a local environment must be regression 
tested in production on the live website.

#### **Assumptions and Dependencies**
Testing is dependent on the website being deployed live on Heroku.


### Test Results

Results to be found in: (/workspace/ms3-seriesdb/testing)

****
## Deployment

### Project Creation
To create this project I used Code Insitute Gitpod Full Template by navigating 
[here](https://github.com/Code-Institute-Org/gitpod-full-template) and clicking the 'Use this template' button.

I was then directed to the create new repository from template page and entered in my desired repo name, then 
clicked Create repository from template button.

Once created, I navigated to my new repository on GitHub and clicked the Gitpod button which built my workspace.

I then created a Python virtual environment to work with this project separately with its own dependencies.

The following commands were used for version control throughout the project:

* git add *filename* - This command was used to add files to the staging area before committing.

* git commit -m "commit message explaining the updates" - This command was used to to commit changes to the local repository.

* git push - This command is used to push all committed changes to the GitHub repository.


### Deployment to Heroku

**Create application:**
1. Navigate to Heroku.com and login.
1. Click on the new button.
1. Select create new app.
1. Enter the app name.
1. Select region.

**Set up connection to Github Repository:**

1. Click the deploy tab and select GitHub - Connect to GitHub.
1. A prompt to find a github repository to connect to will then be displayed.
1. Enter the repository name for the project and click search.
1. Once the repo has been found, click the connect button.

**Set environment variables:**

Click the settings tab and then click the Reveal Config Vars button and add the following:

1. key: IP, value: 0.0.0.0
2. key: PORT, value: 5000
3. key: MONGO_DBNAME, value: (database name you want to connect to)
4. key: MONGO_URI, value: (mongo uri - This can be found in MongoDB by going to clusters > connect > connect to your application and substituting the password and 
    dbname that you set up in the link).
5. key: SECRET_KEY, value: (This is a custom secret key set up for configuration to keep client-side sessions secure).

**Enable automatic deployment:**
1. Click the Deploy tab
1. In the Automatic deploys section, choose the branch you want to deploy from then click Enable Automation Deploys.

### Run Locally

**Note: The project will not run locally with database connections unless the user sets up an [env.py](https://pypi.org/project/env.py/) file configuring IP, PORT, 
MONGO_URI, MONGO_DBNAME and SECRET_KEY. You must have the connection details in order to do this. These details are private and not disclosed in this repository 
for security purposes.**

1. Navigate to the GitHub [Repository](https://github.com/SebastianTirsen/ms3-seriesdb).
1. Click the Code drop down menu.
1. Either Download the ZIP file, unpackage locally and open with IDE (This route ends here) OR Copy Git URL from the HTTPS dialogue box.
1. Open your developement editor of choice and open a terminal window in a directory of your choice.
1. Use the 'git clone' command in terminal followed by the copied git URL.
1. A clone of the project will be created locally on your machine.

Once the project has been loaded into an IDE of choice, run the following command in the shell to install all the required packages:
> pip install -r requirements.txt

### Fork Project 

Most commonly, forks are used to either propose changes to someone else's project or to use someone else's project as a starting point 
for your own idea. - Definition from [Github Docs](https://docs.github.com/en/free-pro-team@latest/github/getting-started-with-github/fork-a-repo).

1. Navigate to the GitHub Repository you want to fork.
1. On the top right of the page under the header, click the fork button.
1. This will create a duplicate of the full project in your GitHub Repository.

****

## Credits

### **Content**

## Graphic & Design Credits

Hero image - Taken from [The New Daily](https://1v1d1e1lmiki1lgcvx32p49h8fe-wpengine.netdna-ssl.com/wp-content/uploads/2016/06/ned-stark-game-of-thrones-740x385.jpg)

Theme Template:
(https://startbootstrap.com/theme/clean-blog)


### Code

Code Istitute, Walk-through, "Boutique Ado".

### **Acknowledgements**

I'd like to express my deepest grattitude to the the following people for their help with my project:

* All the members of Tutor Support for great help and learning.
* My friend Ivan Persson for giving me tips and believing in me.
* My family Therese and Gabriel for support and patience.
* My mentor Daisy McGirr for all her help, compassion, understanding and endless patience.

****