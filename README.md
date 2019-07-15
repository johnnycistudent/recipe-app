# Data-Centric Development Milestone Project

Welcome to my Data-Centric Development Milestone Project which I have entitled "Recipe Book". The purpose of this project is to create an interactive database of recipes that allows users to create, read, update and delete (CRUD) recipes. Recipe Book can be used for general browsing by non-registered users or the users can create an individual account to avail fully of all the features of the website.   

Recipe Book can be accessed here: [https://my-recipe-db.herokuapp.com/](https://my-recipe-db.herokuapp.com/)

## UX


#### Strategy
*WHY does this site exist? And for who? (Target Audience) Detail goal of creator/user.*  
The idea behind this website is to have an online resource to store, look up, create and save recipes. As with any good idea, the basic premise is simple and the user should find it simple to use if it is to be successful. The target audience for this website is any one who needs to store recipes online. The advantages of an online recipe book are numerous as online resources are consistenly replacing more traditional media such as books or magazines. The User stories [here](#user-stories) outline some of the main goals that users of this site would look to achieve.

#### Scope
*WHAT are we doing? Outline features and functions that help achieve goals from Strategy.*  
I chose a Non-relational database in the form of MongoDB for this project.  
###### Functional requirements
The most basic requirements for this project are the ability to perform CRUD (Create, Read, Update and Delete) operations on the primary documents in this database - the recipes. The user should also be able to search the database with relative ease, including queries and searching the entire database with pagination where necessary.  

Although having a user registration function was not necessarily required for this project, I believed it was important to have it to be able to properly implement an integral resource - specifically for the creation and deletion of recipes. This decision meant that there needed to be two views for the target audience of the site; Registered Users and Non-registered Users. The majority of the functionality of the website would be aimed at the registered user. The non-registered user would be able to view recipes but not be able to create, edit, save or delete recipes. This would create accountability and protection for recipe documents. The User collection also gives the option for any user to view all the recipes made by one User.   

I created a third collection to back up the deleted recipes in order to give the Users freedom to delete recipes but the Admin would also have the ability to restore a deleted recipe if they saw fit. The Admin would need a the ability to oversee the changes that have happened to the database i.e. Recipes that have been deleted, no of recipes/users/deleted recipes.   

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

The five primary functions are represented in the Navbar links; Browse Recipes, My Recipes(User created recipes), My Favourites, Add a Recipe and the Log Out function. If the Admin is logged in, the Admin's reports area are represented in the Navbar links to under "Admin Area". The only pages not represented in the Navbar links are the individual Recipes page (including edit recipe) and the view of another Users' recipes i.e. other Users' profile page. For the Admin, the deleted recipe view page is also not represented in the Navbar. Otherwise, all of the users' wants from the website should be easily clicked from the page they are currently on. The browse recipes page is linked in the Brand name at the top left of the page and is essentially the home page. 

Non-registered Users can have only the Login, Register and Browse Recipes pages linked in the Navbar. 

#### Surface
*What will the finished product look like?*
*What colours, typography and design elements will be used?*

Repeating the mantra "keep it simple stupid", I used the Sandstone theme from [Bootswatch](https://bootswatch.com/sandstone/) and adjusted it fit my site's needs. I felt this theme was understated enough in its subtle tones to allow the website's content to flourish. The dark grey navbar and footer colour provides the upper and lower margins of the page and the white background allowed the vibrant colour of the buttons to stand out on the page and draw the users' eyes to call to action components.

The recipes' cards represent the vital stats and the use of FontAwesome's iconography is used liberally throughout the site and reinforce its simplicity to the user. The cards themselves are large and made to stand out with the box shadowing around them and indicate their importance to the user. The cards were inspired by [this demo](https://codepen.io/ahmedhosna95/pen/rZKLgg) on [FreeFrontEnd.com](https://freefrontend.com/) although I did not copy the code from this demo, I only took inspiration from the styling. 

The buttons through out the whole site are shaded and hoverable in four main colours; a navy blue, a bright vibrant blue and pink. The danger buttons are in a stark red. They are designed to make the user want to click them and they also benefit from the box shadow effect. 

The pink colour is used to make vital statistics stand out next to the dark grey font colour of the main text. The largest three headings (H1, H2, H3) all have text shadowing as well as the pink card stats. The font used for the main body and headings is Roboto from Google Fonts. The only other font used on the site is the intro page heading Roboto Slab. The majority of the headings on the site have a font-weight of 700 and appear in the centre of the screen, except the heading above the input fields on the edit/add recipe pages. 



## User Stories

  **1.** As a non-registered user, I would like to browse recipes the site has to offer without signing up.  
  **2.** As a registered or non-registered user, I would like some suggestions as to what recipes other users are using to get some cooking inspiration. 
  **3.** As a registered or non-registered user, I would like to search the database with a query and have the results match my text search. 
  **4.** As a registered or non-registered user, I would like to be able to browse the profile and recipes of a User who has added recipes that I like. 
  **5.** As a registered user, I would like to save recipes that I like and find them with ease. 
  **6.** As a registered user, I would like to be able to have the recipes I've made compiled in one go to page. 
  **7.** As a registered user, I would like to edit or delete a recipe I have added to the site. 
  **8.** As the Administrator of the site, I would like to be able to see the vital statistics of the site in one comprehensive and interactive list. i.e. how many recipes there currently are, how many users, how many deleted recipes etc. 

                


## Wireframes

As mentioned in the [Skeleton](#skeleton) above, here are the wireframes. 

 * [Mobile Wireframes](https://github.com/johnnycistudent/recipe-app/blob/master/static/images/Mobile%20Wireframes%20PDF.pdf)
 * [Desktop Wireframes](https://github.com/johnnycistudent/recipe-app/blob/master/static/images/Desktop%20Wireframes%20PDF.pdf)



## Features

### Existing Features

  *   **User Accounts**
  *   **Search bar** - The Search bar...
  *   **Footer** - The Footer...

### Features Left to Implement

  * Filter by tags
  * Delete recipe restore
  * User ability to upload their own photos
  * 

## Technologies Used
* [HTML](https://www.w3schools.com/html/html5_intro.asp) - [CSS](https://www.w3schools.com/css/) - [Javascript](https://www.w3schools.com/js/)

    This website is written using HTML, CSS and Javascript.

* [Cloud9](https://c9.io/login)

    This website was written on Cloud9. 

* [Bootstrap](https://getbootstrap.com/docs/4.3/getting-started/introduction/)

    This website uses Bootstrap 4.1.3 for its framework. 

* [Bootswatch](https://bootswatch.com/)

    This website uses elements from Bootswatch to build the likes of the Navbar and the buttons.

* [JQuery](https://jquery.com/)

    This website uses JQuery which helps implement javascript features from Bootstrap and the Google Maps Javascript API. 
    

* [FontAwesome](https://fontawesome.com/)

    This website uses icons from FontAwesome in the Hero Image and the GitHub icon in the footer.

* [Google Fonts](https://fonts.googleapis.com/css?family=Muli:400,700i|Poppins:400,400i)

    This website uses...

* [GitHub](https://github.com)

    This website's repository is published on GitHub.   
    
* [Heroku](https://www.heroku.com/)

    This website is hosted and deployed on Heroku. 

## Testing

### Testing User Stories

  * As a user,...  
    **i.** 
    **ii.**   
    **iii.**  
    **iv.** 

  * As a user,...  
    **i.**   
    **ii.** 
    **iii.**    
    **iv.**   

  * As a user, I want to be able to...
    **i.** 
    **ii.** 
    **iii.**   

  * As a user, I want...  
    **i.**   
    **ii.**  
    **iii.**

### Responsiveness
  * I have tested out the responsivesness of the website on Google Chrome, Microsoft Edge and Mozilla Firefox using Dev tools, as well as testing it on Safari on various iOS devices. I have also tested the website on the devices below, both in horizontal and vertical view ports and they have all worked nicely.
   
    * Small devices - iPhone 6s, Samsung J5, Samsung S9. 
    * Medium devices - iPad, Samsung Tablet. 
    * Large/Extra Large devices - Lenovo ideapad 520, Asus Vivobook.  

### Bugs
  * Search showing incorrect results - when an author publishes a new recipe, for example "chicken wings", when a user searches for "chicken" or "wings" etc . 
  * When...
  * When making the function that removes a users' favourite recipes from their profile page, I could only remove recipes from the current or very recent session. When I cleared the cache or used a different browser, I found I could not reach the recipe with the code I had written. I solved this by...

### Validation

  * I have validated my html code through [https://validator.w3.org/](https://validator.w3.org/) and my css code through [http://jigsaw.w3.org/css-validator/](http://jigsaw.w3.org/css-validator/) and no errors have occurred.

## Deployment
The code for this website was pushed from Cloud9 to a repository in GitHub and is published on Heroku where you can access it here:
[https://my-recipe-db.herokuapp.com/](https://my-recipe-db.herokuapp.com/)



## Credits
This website was designed by John O'Connor. 

### Content

### Media 
  All of the images on this page were taken from Pixabay and were sourced using google image search under the free to use search setting. They can be found at the following links  
  
   - []().   

   - []().  
   
   - []().   
   
   - []().   
   
   - []().  

  The favicon image was found at [https://icons8.com/icons/set/cookbook](https://icons8.com/icons/set/cookbook).


## Acknowledgements

  * Bootstrap was used for the framework for this website. [https://bootswatch.com/](https://bootswatch.com/)
  * [Stack Overflow](https://stackoverflow.com/), [W3Schools](https://www.w3schools.com/) and [Slack](https://slack.com/) were very useful when coming up against problems that many other people had also encountered.
  * The Social Media links in the footer were taken and edited from [this link at Bootsnipp.com](https://bootsnipp.com/snippets/84kpo)
  * The code for the User Login, Registration, User Authentication, Profile and Admin Pages functions were all taken and modified from Miroslav Svec's (username Miro) sessions from the Slack channel Data-Centric-Dev. 
  * The logic for the pagination was inspired by Shane Muirhead and Heather Olcott's milestone projects. I was also inspired by Heather for her delete recipe process, which removed the deleted recipe from the recipe DB but first added it to another back up Database.
  * The recipe cards were inspired by [this demo](https://codepen.io/ahmedhosna95/pen/rZKLgg) on [https://freefrontend.com/css-cards/](https://freefrontend.com/css-cards/). 
  * The large button group for the Intro page was taken from Bootsnipp from the following link [https://bootsnipp.com/snippets/GqBjl](https://bootsnipp.com/snippets/GqBjl) and the button styling was made with a button generator at [http://blog.koalite.com/bbg/](http://blog.koalite.com/bbg/)
  * The logic for the Recommended Section on the Browse All recipes page was taken from MongoDB's documentantion - [Here](https://docs.mongodb.com/manual/tutorial/aggregation-with-user-preference-data/#return-the-five-most-common-likes).
  * I looked to various sources for UX theory and inspiration but mostly returned to [UX Planet](https://uxplanet.org/). 

