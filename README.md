# Data-Centric Development Milestone Project

Welcome to my Data-Centric Development Milestone Project which I have entitled "Recipe Book". The purpose of this project is to create an interactive database of recipes that allows users to create, read, update and delete (CRUD) recipes. Recipe Book can be used for general browsing by non-registered users or users can register and create an individual account to avail fully of all the features of the website.   

Recipe Book can be accessed here: [https://my-recipe-db.herokuapp.com/](https://my-recipe-db.herokuapp.com/)

## UX


#### Strategy
*WHY does this site exist? And for who? (Target Audience) Detail goal of creator/user.*  
The idea behind this website is to have an online resource to store, look up, create and save recipes. As with any good idea, the basic premise is simple and the user should find it simple to use if it is to be successful. The target audience for this website is any one who needs to store recipes online. The advantages of an online recipe book are numerous as online resources are consistenly replacing more traditional media such as books or magazines. The User stories [here](#user-stories) outline some of the main goals that users of this site would look to achieve.

#### Scope
*WHAT are we doing? Outline features and functions that help achieve goals from Strategy.*  
I chose a Non-relational database in the form of MongoDB for this project.  
###### Functional requirements
The most basic requirements for this project are the ability to perform CRUD (Create, Read, Update and Delete) operations on the primary documents in this database - the recipes. The user should also be able to search the database with relative ease, including queries and navigating the entire database with pagination where necessary.  

Although having a user registration function was not necessarily required for this project, I believed it was important to have it to be able to properly implement an integral resource - specifically for the creation and deletion of recipes. This decision meant that there needed to be two views for the target audience of the site; Registered Users and Non-registered Users. The majority of the functionality of the website would be aimed at the registered user. The non-registered user would be able to view recipes but not be able to create, edit, save or delete recipes. This would create accountability and protection for the documents in the Recipe collection. The User collection also gives the option for any user to view all the recipes made by one User.   

I created a third collection to back up the deleted recipes in order to give the Users freedom to delete recipes but the Admin would also have the ability to restore a deleted recipe if they saw fit. The Admin would need the ability to oversee the changes that have happened to the database i.e. Recipes that have been deleted, no of recipes/users/deleted recipes and other relevant information.   

The site should be responsive and work on all browsers.   

###### Content requirements
The content requirements for the functions proposed above would be as follows:
  - A search box for users queries. 
  - A recipe display view, that lays out the content of each individual recipe with all the fields present.
  - Add a recipe form page.
  - Edit a recipe page. 
  - User profile view.
  - User favourites page.
  - Registration/Login box.
  - Log Out button. 
  - Admin view. 

#### Structure
*HOW - How much content is there, how is it organised, how is it prioritised, interaction design and architecture*  

The information architecture of the database consists of three collections - Recipes, Users and Deleted. When a User creates a recipe, their username and ObjectId is saved as a nested object within that Recipe document under the field "author". Using the same logic, when a User deletes a recipe, their ObjectId and Username is logged as a nested object under the field "deleted_by" in that Deleted recipe document. When a User saves a recipe as a favourite, the recipe's ObjectId is saved in an array in the recipe document under the field "favourite_recipes". The recipe has a field called "favourite_count" which increments by one every time a User adds that recipe to their favourite recipe array. When a recipe is deleted, the recipe is deleted from User's favourites as well as the recipe collection and the favourite count is reset to 0. See the schema below:

1. Recipe 
  ```
{
          "_id": ObjectId("5d000a2c288d0f000cff5ab3"),
          "recipe_name": "Jerk Cod & Creamed Corn",
          "photo_url": "https://www.bbcgoodfood.com/sites/default/files/styles/recipe/public/recipe/recipe-image/2019/05/jerk-cod-creamed-corn.jpg?itok=gYbt_V5u",
          "preptime": "12 mins",
          "servings": "2 ",
          "calories": "339 ",
          "fat": "14 ",
          "satfat": "None ",
          "carbs": "21 ",
          "fiber": "6 ",
          "sugar": "12 ",
          "protein": "29 ",
          "ingredients": [
              "2 thick cod fillets (around 120g each)",
              "1 tbsp olive oil"
              "2 tsp jerk seasoning"
              "Bunch spring onions"
              "326g can sweetcorn drained"
              "2 tbsp single cream"
              "20g parmesan, finely grated"
              "1/2 small red chilli, deseeded and finely chopped"
              "1/2 small bunch coriander, finely chopped"
              "Life wedges to serve"
          ],
          "instructions": "Heat the oven to 200C/180C fan/gas 6. Put the cod on a baking sheet and rub with half the oil, the jerk seasoning and some salt and pepper. Cook for 12-15 mins until cooked through and flaking.\r\n\r\nMeanwhile, heat a griddle pan or non-stick frying pan over a high heat. Rub the remaining oil over the whole spring onions. Add to the pan and cook for 8-10 mins or until charred and beginning to soften. Keep warm on a plate.\r\n\r\nPut the corn in a saucepan with the cream and warm through for 2 mins. Using a stick blender, roughly blitz the corn to a semi-smooth consistency. Stir though the parmesan, chilli and half the coriander, then season to taste. \r\n\r\nServe the cod with the charred spring onions, creamed corn and lime wedges for squeezing over, and scatter over the remaining coriander.",
          "tags": [
              "Healthy ",
              "Pescatarian"
              "Quickdinner"
          ],
          "added_on": ISODate("2019-06-11T20:08:12.441Z"),
          "author" : {
                      "_id" : ObjectId("5d000706288d0f000cff5ab2"),
                      "username" : "Ciara mac"
              },
          "favourite_count": int(1)
}
  ```
2. Users
```
{
        "_id" : ObjectId("5d18c050596178940bce23b8"),
        "username" : "Susan",
        "email" : "blank@gmail.com",
        "password" : "pbkdf2:sha256:150000$fXtPBrA5$22a45318628c1f6580aa44b12bc3c84e8c3710cbdea8922b96e482f4ddb91b77",
        "favourite_recipes" : [
                ObjectId("5d18c67e596178940bce23b9"),
                ObjectId("5cfe4783abef1e0a5e0461a7")
        ]
}
```
3. Deleted
```
{
        "_id" : ObjectId("5cdc3ff7abef1e09dde7c510"),
        "recipe_name" : "iPhone Recipe Test",
        "photo_url" : "https://www.gimmesomeoven.com/wp-content/uploads/2014/03/Cajun-Jambalaya-Recipe-with-Andouille-Sausage-Shrimp-and-Chicken-3-1.jpg",
        "servings" : "",
        "calories" : "",
        "preptime" : "",
        "protein" : "",
        "fiber" : "",
        "photo_url" : "",
        "ingredients" : [
                ""
        ],
        "instructions" : "",
        "tags" : [
                ""
        ],
        "satfat" : null,
        "carbs" : "",
        "fat" : "",
        "sugar" : "",
        "deleted_on" : ISODate("2019-07-02T11:13:34.045+00:00"),
        "deleted_by" : {
                "_id" : ObjectId("5cdbfcb4abef1e06e05c1da2"),
                "username" : "John"
        }
        "favourite_count": int(0)
}
```

The interaction design for this site tries to keep things as simple as possible. The Initial page entitled Intro presents the three main steps for a user in big tempting, clickable buttons - Browse Recipes, Login or Register. The navigational structures from the Navbar are standard and should be familiar with all browser users that collapse to a hamburger menu on smaller devices. It was important to ensure that the user is presented with as many interactive elements as possible when navigating the site. 

Once the User logs in or registers, they are immediately sent to their profile page. From there they are encouraged to go to the "Browse Recipes" page.

The main focus of the Recipe Book are the recipes themselves. As with all good UX design, most components advertising the recipes should be interactive and if they are interactive, it should be obvious to the user. This effect is obtained on this website by changing the cursor to a pointer and having buttons hoverable if active.  The recipe name and photo are clickable as well as a button offering to "View Full Recipe" and will all take the user to the full recipe view - "Recipe Display". The User then has further options to favourite, edit or delete the recipe, all choices displayed on buttons below the photo and vital recipe statitics. 

Within the User's My Recipes and My Favourites, they are consistenly encouraged to add new recipes or add favourites with buttons that will take them to the add recipe and browse more recipe pages respectively. When a User adds a new recipe, they are immediately returned to the view of that recipe and when they go to browse all recipes, their recipe appears at the top of all the recipes.

The search function keeps the user informed about the results of their queries. It displays a message reminding the User of their exact search term and informs them of the number of results. If the User's query produces no results, they are encouraged to try one of the site's most popular recipes. This is the way the recipes are rated on the site. 

I have tried to rely on the 3 Click Rule as much as possible. Each interaction should bring the user to their desired need and if not, they're next navigational choice should be suggested to keep them from becoming frustrated. If all else fails, the navbar links should make it easy to fall back on the main functions of the site.


#### Skeleton
*How is the information structured? How is it logically grouped?*

The information structure is laid out in the wireframes below:

 * [Mobile Wireframes](https://github.com/johnnycistudent/recipe-app/blob/master/static/images/Mobile%20Wireframes%20PDF.pdf)
 * [Desktop Wireframes](https://github.com/johnnycistudent/recipe-app/blob/master/static/images/Desktop%20Wireframes%20PDF.pdf)

The five primary functions are represented in the Navbar links; Browse Recipes, My Recipes(User created recipes), My Favourites, Add a Recipe and the Log Out function. If the Admin is logged in, the Admin's reports area are represented in the Navbar links under "Admin Area". The only pages not represented in the Navbar links are the individual Recipes page (including edit recipe) and the view of another Users' recipes i.e. other Users' profile page. For the Admin, the deleted recipe view page is also not represented in the Navbar. Otherwise, all of the users' wants from the website should be easily clicked from the page they are currently on. The browse recipes page is linked in the Brand name at the top left of the page and is essentially the home page. 

Non-registered Users can have only the Login, Register and Browse Recipes pages linked in the Navbar. 

#### Surface
*What will the finished product look like?*
*What colours, typography and design elements will be used?*

Repeating the mantra "keep it simple stupid", I used the Sandstone theme from [Bootswatch](https://bootswatch.com/sandstone/) and adjusted it fit my site's needs. I felt this theme was understated enough in its subtle tones to allow the website's content to flourish. The dark grey navbar and footer colour provides the upper and lower margins of the page and the white background allowed the vibrant colour of the buttons to stand out on the page and draw the users' eyes to the call to action components.

The recipes' cards represent the vital stats and the use of FontAwesome's iconography is used liberally throughout the site and reinforces its simplicity to the user. The cards themselves are large and made to stand out with the box shadowing around them and indicate their importance to the user. The cards were inspired by [this demo](https://codepen.io/ahmedhosna95/pen/rZKLgg) on [FreeFrontEnd.com](https://freefrontend.com/) although I did not copy the code from this demo, I only took inspiration from the styling. 

The buttons through out the whole site are shaded and hoverable in four main colours; a navy blue, a bright vibrant blue and pink. The danger buttons are in a stark red. They are designed to make the user want to click them and they also benefit from the box shadow effect. 

The pink colour is used to make vital statistics stand out next to the dark grey font colour of the main text. The largest three headings (H1, H2, H3) all have text shadowing as well as the pink card stats. The font used for the main body and headings is Roboto from Google Fonts. The only other font used on the site is the intro page heading Roboto Slab. The majority of the headings on the site have a font-weight of 700 and appear in the centre of the screen, except the headings above the input fields on the edit/add recipe pages. 



## User Stories

  **1.** As a non-registered user, I would like to browse recipes the site has to offer without signing up.  
  
  **2.** As a registered or non-registered user, I would like some suggestions as to what recipes other users are using to get some cooking inspiration.
  
  **3.** As a registered or non-registered vegetarian user, I would like to search the database for vegetarian recipes.    
  
  **4.** As a registered or non-registered user, I would like to be able to browse the profile and recipes of a User who has added recipes that I like. 
  
  **5.** As a registered user, I would like to add a recipe and then be able to view the recipe/recipes I’ve made compiled in one go-to page.    
  
  **6.** As a registered user, I would like to save recipes that I like and find them with ease. 
  
  **7.** As a registered user, I would like to edit or delete a recipe I have added to the site.  
  
  **8.** As the Administrator of the site, I would like to be able to see the vital statistics of the site in one comprehensive and interactive list. i.e. how many recipes there currently are, how many users, how many deleted recipes etc. 
  
  **9.** As the Administrator of the site, I would like to restore a recipe I deleted previously to the active recipe collection. 

                


## Wireframes

As mentioned in the [Skeleton](#skeleton) above, here are the wireframes. 

 * [Mobile Wireframes](https://github.com/johnnycistudent/recipe-app/blob/master/static/images/Mobile%20Wireframes%20PDF.pdf)
 * [Desktop Wireframes](https://github.com/johnnycistudent/recipe-app/blob/master/static/images/Desktop%20Wireframes%20PDF.pdf)



## Features

### Existing Features

  *   **Navbar** - The Navbar offers an easy navigational view through the site for both non-registered and registered users and is always available to act as a reference point for any user not necessarily sure of their whereabouts on the site. 
  *   **Intro Page** - The Intro Page welcomes new Users to the site with a brief explainer and offers three options - Browse Recipes, Log in or Create an Account. 
  *   **Browse All Recipes** - This function and page acts as the home page for the site and is linked by the Brand Name in the top left corner of the Navbar. The recipes are ordered by last added first so users can see their latest recipes feature full prominence on the site to encourage user activity inclusion.
  *   **Search bar** - The Search bar on the Browse Recipes page is designed to match the text query of the user. The results of the user's queries follow best practices of UX design - the user is reminded of their query and informed of the number of results their query has generated. The search submit button can be triggered by the return or enter key on any device that the site is being viewed through.
  *   **Full Recipe Display** - The full recipe view is rendered when a registered or non registered user clicks on one of the cards displaying a recipes' information. The user is then taken to a page dedicated to only that particular recipe where all the recipe information is presented. This page offers many options to the registered user - Add Recipe to Favourites, Edit the Recipe or Delete it. It also offers both registered and non-registered Users the option to view the recipe author's other additions to the site by clicking on their username. 
  *   **User Accounts** - Each user has the ability to create their own account which enables them to access a wider array of features on the website such as saving(favouriting), editing, deleting and creating recipes. 
  *   **Add and Edit Recipes** - Satisfying the Create and Update part of CRUD functions required for this site, registered users can add a new recipe to the site and also edit any one's recipes by interacting with the recipe forms, 
  *   **Favourite/Save Recipes** - Registered users can easily save recipes they like and want to refer to later. The recipes are stored in the "My Favourites" page which is represented in the Navbar so easy to navigate to. The ability to "favourite" a recipe ties in with the rating system in the Most Popular section, mentioned next. 
  *   **Most Popular Recipes Section** - The Most Popular section is designed to promote the most "favourited" recipes on the site, to inspire users to add to their favourites or give ideas for adding their own recipes and also as a recipe rating system. It appears when the User has no favourites on their "My Favourites" page, at the top of the browse all recipes page and when a user's search query returns no results. The Most Popular recipes appear on bootstrap customised cards in the same way the rest of the recipes on the site are represented except they also display the number of times the recipes have been favourited. 
  *   **Delete Recipes** - Because a recipe that is deleted is sent to a back up collection called "Deleted",  Registered users can delete any recipe from the website. If a recipe is deleted, it is removed from any users that may have it stored in their "My Favourites" and the recipes' favourite count field is reset to zero. 
  *   **Deleted Recipe View/Restore Deleted Recipes** - The Admin has the ability to review deleted recipes and restore them if they see fit. 
  *   **User Profiles** - The User Profile is used to view your own recipes as well as other user's recipes. The "My Recipes" link in the navbar allows the user to view the recipes they themselves have added. As mentioned in the Full Recipe Display feature above, if a user wants to view another user's profile, they can follow the link by clicking on the name of the recipe author displayed on the full recipe display. 
  *   **Admin Area** - The Admin Area allows the site Administrator to view a list of information/statistics about each collection in the database. The information includes the total number of documents in each collection, each document and a link to said document as well as the date each document was created. This view also links each user profile as well as offering a path to the deleted recipe display, where the deleted recipe can be restored. 
  *   **Footer** - The footer features links to the social media accounts of myself, the site developer and my Github profile. 

### Features Left to Implement

  * Comments section on recipes
  * User ability to upload their own photos
  * User ability to edit their own profile, change username or email and reset their password

## Technologies Used
* [HTML](https://www.w3schools.com/html/html5_intro.asp) - [CSS](https://www.w3schools.com/css/) - [Javascript](https://www.w3schools.com/js/) - [JQuery](https://jquery.com/) - [FontAwesome](https://fontawesome.com/) - [Google Fonts](https://fonts.googleapis.com/css?family=Muli:400,700i|Poppins:400,400i)

    This site's front end is written using HTML, CSS, Javascript and Jquery. It features iconography from FontAwesome's library and fonts from Google Fonts. 

* [Bootstrap](https://getbootstrap.com/docs/4.3/getting-started/introduction/) - [Bootswatch](https://bootswatch.com/)

    This website uses Bootstrap 4.1.3 and elements from Bootswatch to build the likes of the Navbar and the buttons for its framework and for responsivesness. 

* [AWS Cloud9](https://aws.amazon.com/cloud9/)

    The IDE this website was written on is AWS Cloud9. 

* [GitHub](https://github.com) - [Heroku](https://www.heroku.com/) - [Flask](http://flask.pocoo.org/) - [Jinja Python Templates](http://jinja.pocoo.org/) - [Python](https://www.python.org/)

    This website's Git repository is published on GitHub and is deployed on Heroku. The backend code is written in Python and Flask is used as the Python web framework and uses Jinja templates.
    
* [MongoDB](https://www.mongodb.com/) - [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)    

    MongoDB is the NoSQL database used for this site and is hosted by MongoDB Atlas. 

    

## Testing

### Testing User Stories

1. As a non-registered user, I would like to browse recipes the site has to offer without signing up.  

   **i.** From the opening page - [http://my-recipe-db.herokuapp.com/](http://my-recipe-db.herokuapp.com/) - click on either the large "start Cooking" button that's prominent on the screen, click the "Browse Recipes" navbar link or click the Recipe Book brand name at the top left of the navbar.  
   **ii.** Scroll down to the Browse All Recipes section after following one of the above paths and peruse the recipe cards.  
   **iii.** Skip through the pages at the bottom of the page using the pagination controls. 
  
2. As a registered or non-registered user, I would like some suggestions as to what recipes other users are using to get some cooking inspiration.  

   **i.** As a non-registered or registered user, if I navigate to the browse recipe page, the top of the page features the Most Popular section, featuring the 3 Most Popular recipes on the site.  
   **ii.** As a non-registered or registered user, if I enter a search query with no results - for example, just by clicking on the search submit button with no query in the input field, the search will produce no results but will offer up the Most Popular section as a method of inspiration to users.     
   **iii.** As a registered user, if I log in for the first time I will be taken to My Favourites page which will have no favourites. As long as I have not added any favourites, the Most Popular section will appear.   
  
3. As a registered or non-registered vegetarian user, I would like to search the database for vegetarian recipes. 

   **i.** Navigate to the browse recipe section.  
   **ii.** Type "vegetarian" into the input field and submit the search query.   
   **iii.** Browse the results.   

  
4. As a registered or non-registered user, I would like to be able to browse the profile and recipes of a User who has added recipes that I like. 

   **i.** Browse the site's recipes and find a recipe you like.  
   **ii.** Click into the recipe's full view.   
   **iii.** Navigate to the Added By field on the form and click the Username which will be hyperlinked and will go to the recipe author's profile page.   
   **iv.** Browse the profile of the recipe's author.     
   
5. As a registered user, I would like to add a recipe and then be able to view the recipe/recipes I've made compiled in one go-to page.

   **i.** Navigate to the Add a Recipe page, either by the navbar link or the suggestion button in the My Recipe page.   
   **ii.** Fill out the form and submit the new recipe and you will be taken to the new recipe display.   
   **iii.** Either click on the navbar link entitled "My Recipes" or click on your own username displayed at the Added By field (as per the previous user story).     
   **iv.** Browse the recipes you have added.   

6. As a registered user, I would like to save recipes that I like and find them with ease.  

   **i.** Browse the site's recipes and find a recipe you like.   
   **ii.** Click into the recipe's full view.     
   **iii.** Navigate to the Add to Favourites button below the recipe's photo and click.    
   **iv.** The page will refresh with an alert informing you of the recipe has been added to your favourites.  
   **v.** Navigate to your favourites page by clicking the navlink entitled My Favourites and check the recipe has been added.   
   **vi.** Ensure the recipe cannot be added to your favourites again if it's already there by clicking on the Add to Favourites button again.   
   **vii.** The page should refresh and inform you that the recipe has already been added to your favourites.   
   **viii.** Double check the recipe hasn't been added to your favourites by navigating to your My Favourites page again and ensure the recipe is only present once.   

7. As a registered user, I would like to edit or delete a recipe I have added to the site.   

   **i.** Browse the site's recipes and find a recipe you want to edit/delete. It may be advisable to add a test recipe for the sake of this user story.   
   **ii.** Click into the recipe's full view and click the Edit Recipe button.    
   **iii.** Edit as many fields as you see fit, delete and add ingredients and tags to ensure their dynamic field inputs are working.   
   **iv.** Submit the edited recipe and you will be returned to the newly edited recipe. Ensure your changes have taken effect.   
   **v.** In order to delete this recipe, click on the Delete Recipe button beside the Edit Recipe button. BUT first, add the recipe to your favourites by clicking the Add to Favourites in order to check that when you delete this recipe, it will be removed from your favourites page.   
   **vi.** A "Delete Recipe" Modal will pop up asking are you sure you want to delete this recipe. Click on "No, go back" to make sure the cancel option works or click anywhere else on the screen and watch the modal disappear.   
   **vii.** Click on "Yes, Delete" to delete the recipe and you will be returned to the browse recipes page where an alert will inform you the recipe has been deleted.   
   **viii.** Search the database for the recipe you have just deleted to ensure it has been removed from the site.  
   **ix.** Check your My Favourites page for the recipe you have just deleted to make sure it has been removed from there too.   
   
  
8. As the Administrator of the site, I would like to be able to see the vital statistics of the site in one comprehensive and interactive list. i.e. how many recipes there currently are, how many users, how many deleted recipes etc.   

   **i.** If you are logged in as an active user, log out by clicking the Log Out at the top right hand corner of the navbar.      
   **ii.** Navigate to the Login page either by the navbar link or the "Sign In" button on the Intro page.      
   **iii.** To Log in as the Administrator, type "admin" in to the username field, and "thisismypassword" in to the password field and submit. Ensure both username and password are all lowercase.      
   **iv.** Confirm you have been logged in as the Administrator. You should be taken directly to the Admin Area upon logging in as Admin but if not, click Admin Area in the navbar link.   
   **v.** Browse through the User, Recipes and Deleted Recipes reports in the accordion-style table.    
   **vi.** Ensure all hyperlinks work - a view to each User's profile, a view to each Recipe display and a view to each Deleted Recipe.   
  
9. As the Administrator of the site, I would like to restore a recipe I deleted previously to the active recipe collection.   

   **i.** Following on from the above User story, remain logged in as the Administrator and stay on the Admin Area page.    
   **ii.** Navigate to the Deleted Recipe view by clicking on the "Deleted Recipes Report" tab on the report table and click on the hyperlinked name of a recipe you would like to restore.   
   **iii.** Click on the only button in red on the page entitled "Restore Recipe".   
   **iv.** Like the Delete Recipe process, a Modal will appear asking if you are sure you would like to restore this recipe. Click Yes, Restore.   
   **v.** You will be taken back to the Browse Recipes page and a message will appear stating the recipe has been restored.   
   **vi.** Search the database for the restored recipe to ensure it has successfully been re-instated.   

### Responsiveness
  I have tested out the responsivesness of the website on Google Chrome, Microsoft Edge and Mozilla Firefox using Dev tools, as well as testing it on Safari on various iOS devices.  
  The Recipe cards were designed to help the responsiveness of the site. On mobile view, the screen displays one recipe per column, on medium devices two cards are displayed and then three cards are displayed on anything larger. Bootstrap's grid system was very useful in this regard and meant the only media query I needed for the whole site was for the Admin Area info table.
  The tests took place on the devices below, both in horizontal and vertical view ports. All buttons and links work on all devices.  
   
    * Small devices - iPhone 6s, Samsung J5, Samsung S9. 
    * Medium devices - iPad, Samsung Tablet. 
    * Large/Extra Large devices - Lenovo ideapad 520, Asus Vivobook.  

### Bugs
  Most of the bugs I encountered while developing this site had to do with how I previously stored the "Favourited Recipes". Initially, when a User saved a recipe, that recipe Object would be saved as an object in an array called "favourite_recipes". Using the similar logic, when a User published a new recipe, I would match their session username with their User "username" and save their entire User document as an object in an array within that particular recipe document called "author".  
  This produced the following bugs when I asked family and friends to test my site:
  * User search queries were showing incorrect results. Because my search function is based on text match, if a user published a new recipe called "Chicken wings", that recipe would appear in a search query that didn't mention "chicken" or "wings". I realised that this was because the User object saved in the "author" array of objects was triggering the search query. The user's "favourite_recipes" array had the chicken wings recipe embedded in it and was distorting the source. I changed the code so that only the User's username and their ObjectID were saved in the "author" array and fixed the bug. 
  * When making the function that removes a users' favourite recipes from their profile page, I could only remove recipes from the current or very recent session. When I cleared the cache or used a different browser, I found I could not reach the recipe with the code I had written. I also realised that once a recipe was saved in a User's "favourite recipes" array and was subsequently edited, the "My Favourites" recipes would appear different to the actual recipes. 
  I solved both of these problems by changing the way I saved the favourite recipes. I only saved the ObjectID of the recipe once a User saved that recipe to their favourites and then performed a find operation to search the recipe database with the favourited ObjectID/s when rendering the My Favourites page. This fix also solved the problem of being unable to remove favourite recipes from previous sessions.  

### Validation

  * I have validated my html code through [https://validator.w3.org/](https://validator.w3.org/) and my css code through [http://jigsaw.w3.org/css-validator/](http://jigsaw.w3.org/css-validator/) and no errors have occurred.

## Deployment

The app is deployed to Heroku and can be found at the following link: [https://my-recipe-db.herokuapp.com/](https://my-recipe-db.herokuapp.com/)

  - Download the repo for my project or clone it using the following method: 
  - Open a new workspace and download the git repository with the following CLI commands:
  ```
  git clone https://github.com/johnnycistudent/recipe-app.git
  ```
  - This method will put everything into a subfolder so cut and paste the project out of the subfolder and delete the subfolder so all the paths are correct.

  - Ensure "debug" is set to true at the bottom of the app.py file like below:
  ```
  if __name__ == '__main__':
      app.run(host=os.environ.get('IP'),
              port=int(os.environ.get('PORT')),
              debug=True),
  ```
  - Create a New App with Heroku that must have a unique name.
  - Then log into Heroku via cloud9 bash "heroku login" then enter email and password
  - "heroku apps" bash command lets you see what apps you have with heroku
  - Install Flask and pymongo with the following commands in bash:
  - Flask:
  ```
  sudo pip3 install flask
  ```
  - Pymongo:
  ```
  sudo pip3 install pymongo
  ```
  - To get Flask talking to Mongo, we need to install a 3rd party library called flask-pymongo:
  ```
  sudo pip3 install flask-pymongo
  ```
  - We also need to install the dnspython if it isn't already installed:
  ```
  sudo pip3 install dnspython
  ```
  - You can't push to Heroku without a requirements.txt file. Use the below command in bash to do that:
  ```  
  sudo pip3 freeze --local > requirements.txt
  ```
  - Next, add a procfile:
  ```
  echo web: python app.py > Procfile
  ```
  - Then commit to git and push to heroku:
  ```
  git add .
  git commit -m "your commit statement"
  push to heroku "git push heroku master"
  ```
  - Next we want to run our application, enter the following into bash:
```
heroku ps:scale web=1
```
  - Dynos are scaled with this command.
  - Go to heroku and go to settings, and config Vars as follows:
  - Enter IP and set value to 0.0.0.0 
  - Enter PORT as the next key and enter 5000 as value
  - Enter MONGO_DBNAME as key and myRecipeDB as value
  - Enter MONGO_URI as key and mongodb+srv://<username>:<password>@myfirstcluster-2jd1l.mongodb.net/myRecipeDB?retryWrites=true. Update the username and password from the placeholders.
  - Enter SECRET_KEY as key and the appropriate password as the value. 
  - Make sure the below environ variables at the top of the app.py file are set in a hidden folder (.bashrc) or a .gitignore file for security purposes and that they match the config vars from the Heroku App settings:
  ```
    app.config['MONGO_DBNAME'] = 'myRecipeDB'
    app.config['MONGO_URI'] = os.getenv("MONGO_URI")
    app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
  ```
  - Click Open App in Heroku or go to [https://my-recipe-db.herokuapp.com/](https://my-recipe-db.herokuapp.com/).
  - Restart dynos if there are any errors or consult the Heroku error log that appears upon unsuccessful deployment.



## Credits
This website was designed by John O'Connor. Stack Overflow, the Code Institute tutors and the Code Institute Data-Centric Development channel were also extremely helpful during the production of this project.

### Content

### Media 

   - The recipes I used in this website are mostly imported from a GitHub json that can be found [here](https://github.com/tabatkins/recipe-db/blob/master/db-recipes.json). All the recipes photos associated are from that json. 

   - The backup photo for recipes without a photo and the Intro page background were taken from a free search of [Pixabay](https://pixabay.com/).  
   
   - The favicon image was found at [https://icons8.com/icons/set/cookbook](https://icons8.com/icons/set/cookbook).
   
   - Any other photos uploaded by Users were sourced by them.


## Acknowledgements

  * [Stack Overflow](https://stackoverflow.com/), [W3Schools](https://www.w3schools.com/) and [Slack](https://slack.com/) were very useful when coming up against problems that many other people had also encountered.
  * The following documentation that was consulted constantly - [MongoDB Manual](https://docs.mongodb.com/manual/), [Pymongo](https://api.mongodb.com/python/current/) and [Flask](https://flask.palletsprojects.com/en/1.0.x/).
  * The Social Media links in the footer were taken and edited from [this link at Bootsnipp.com](https://bootsnipp.com/snippets/84kpo)
  * The code for the User Login, Registration, User Authentication, Profile and Admin Pages functions were all taken and modified from Miroslav Svec's (username Miro) sessions from the Slack channel Data-Centric-Dev. 
  * The logic for the pagination was inspired by Shane Muirhead and Heather Olcott's milestone projects. I was also inspired by Heather for her delete recipe process, which removed the deleted recipe from the recipe collection but first added it to another back up collection.
  * The recipe cards were inspired by [this demo](https://codepen.io/ahmedhosna95/pen/rZKLgg) on [https://freefrontend.com/css-cards/](https://freefrontend.com/css-cards/). 
  * The large button group for the Intro page was taken from Bootsnipp from the following link [https://bootsnipp.com/snippets/GqBjl](https://bootsnipp.com/snippets/GqBjl) and the button styling was made with a button generator at [http://blog.koalite.com/bbg/](http://blog.koalite.com/bbg/)
  * I looked to various sources for UX theory and inspiration but mostly returned to [UX Planet](https://uxplanet.org/). 

