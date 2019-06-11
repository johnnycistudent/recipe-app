import os, math, datetime
from flask import Flask, render_template, redirect, request, url_for, session, flash, jsonify, json
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'myRecipeDB'
app.config['MONGO_URI'] = os.getenv("MONGO_URI")
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

users = mongo.db.users
recipes = mongo.db.recipes
deleted = mongo.db.deleted

@app.route('/')
def intro():
    return render_template("intro.html")
    
@app.route('/get_recipes')    
def get_recipes():
    
    
    # # Results per page
    p_limit = 6
    current_page = int(request.args.get('current_page', 1))
    collection = mongo.db.recipes.count()
    pages = range(1, int(math.ceil(collection / p_limit)) + 1)
    total_page_no = int(math.ceil(collection/p_limit))
    recipes = mongo.db.recipes.find().skip((current_page -1)*p_limit).limit(p_limit)
    
    return render_template("showall.html", recipes=recipes, current_page=current_page, pages=pages, total_page_no=total_page_no)
    
    
@app.route('/search')
def search():
    p_limit = 9
    current_page = int(request.args.get('current_page', 1))
    
    word_search = request.args.get('word_search')
    results = mongo.db.recipes.find({'$text': {'$search': str(word_search) }}).sort('_id', pymongo.ASCENDING).skip((current_page -1)*p_limit).limit(p_limit)
    results_count = mongo.db.recipes.find({'$text': {'$search': str(word_search) }}).count()
    results_pages = range(1, int(math.ceil(results_count / p_limit)) + 1)
    total_page_no = int(math.ceil(results_count/p_limit))
    
    return render_template("search.html", 
                            current_page=current_page, 
                            results_count=results_count,
                            word_search=word_search,
                            results=results,
                            results_pages=results_pages,
                            total_page_no=total_page_no)    
    
    
@app.route('/recipe_display/<recipe_id>')
def recipe_display(recipe_id):
    recipe = mongo.db.recipes.find_one({'_id':ObjectId(recipe_id)})
    return render_template('recipe_display.html', recipe=recipe)
    

    
    
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    
    if 'user' in session:
    
        recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
        
    else:
        flash("You must be logged in to Edit, Save or Delete a recipe!")
        return redirect(url_for('get_recipes')) 
    
    return render_template('editrecipe.html', recipe=recipe)
    
@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update_one({'_id':ObjectId(recipe_id), 
    }, {
        '$set': {
    'recipe_name':request.form.get('recipe_name'),
    'photo_url':request.form.get('photo_url'),
    'preptime': request.form.get('preptime'),
    'servings': request.form.get('servings'),
    'calories':request.form.get('calories'),
    'fat':request.form.get('fat'),
    'satfat':request.form.get('satfat'),
    'carbs':request.form.get('carbs'),
    'fiber':request.form.get('fiber'),
    'sugar':request.form.get('sugar'),
    'protein':request.form.get('protein'),
    'ingredients':request.form.getlist('ingredients'),
    'instructions':request.form.get('instructions'),
    'tags':request.form.getlist('tags')
    }
    })
    
    flash('Recipe updated.')
    return redirect(url_for('recipe_display', recipe_id=recipe_id))


@app.route('/add_recipe')
def add_recipe():
    recipes=mongo.db.recipes.find()
    return render_template('addrecipe.html', recipes=recipes)
    
@app.route('/insert_recipe', methods=["POST"])
def insert_recipe():  
    recipes = mongo.db.recipes
    user = users.find_one({"username": session['user']})
    new_recipe = recipes.insert_one({
        'recipe_name':request.form.get('recipe_name'),
        'photo_url':request.form.get('photo_url'),
        'preptime': request.form.get('preptime'),
        'servings': request.form.get('servings'),
        'calories':request.form.get('calories'),
        'fat':request.form.get('fat'),
        'satfat':request.form.get('satfat'),
        'carbs':request.form.get('carbs'),
        'fiber':request.form.get('fiber'),
        'sugar':request.form.get('sugar'),
        'protein':request.form.get('protein'),
        'ingredients':request.form.getlist('ingredients'),
        'instructions':request.form.get('instructions'),
        'tags':request.form.getlist('tags'),
        'added_on' : datetime.datetime.utcnow(), 
        'author' : {
            '_id': user['_id'],
            'username': user['username']}
    })
    
    flash('Recipe Added.')
    return redirect(url_for('recipe_display', recipe_id = new_recipe.inserted_id))
    
    
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    
    if 'user' in session:
        
        user = users.find_one({"username": session['user']})
    
        deleted_recipe = recipes.find_one({'_id': ObjectId(recipe_id)})
        
        deleted.insert_one(deleted_recipe)
        
        deleted.update_one({'_id': ObjectId(recipe_id)}, 
                                                {"$set" :
                                                    {"deleted_on" : datetime.datetime.utcnow(), 
                                                    "deleted_by" : {
                                                                '_id': user['_id'],
                                                                'username': user['username']}}
                                                })
        
        recipes.remove({'_id': ObjectId(recipe_id)})
        
    else:
        flash("You must be logged in to Edit, Save or Delete a recipe!")
        return redirect(url_for('get_recipes'))
    
    
    flash('Recipe Deleted.')
    return redirect(url_for('get_recipes'))   
    
    
@app.route('/add_to_favourites/<recipe_id>', methods=["GET", "POST"])
def add_to_favourites(recipe_id):
    
    if 'user' in session:
        
        user = users.find_one({"username": session['user']})
        favourites = user['favourite_recipes']
    
        favourited_recipe = recipes.find_one({'_id': ObjectId(recipe_id)})
        
        if favourited_recipe not in favourites:
            users.update_one({"username": session['user']}, 
                                                    {"$push" :
                                                        {"favourite_recipes" : favourited_recipe}})
        else:
            flash("You have already added this recipe to your Favourites")
            return redirect(url_for('recipe_display', user=user['username'], recipe_id=recipe_id))
    else:
        flash("You must be logged in to Edit, Save or Delete a recipe!")
        return redirect(url_for('get_recipes'))
    
    
    flash('Added to Favourites.')
    return redirect(url_for('recipe_display', user=user['username'], recipe_id=recipe_id))

@app.route('/remove_from_favourites/<recipe_id>', methods=["GET", "POST"])
def remove_from_favourites(recipe_id):
    
    if 'user' in session:
        user = users.find_one({"username": session['user']})
        favourites = user['favourite_recipes']
        
            
        
        remove_recipe = recipes.find_one({'_id': ObjectId(recipe_id)})
        
        if remove_recipe in favourites:
            users.update_one({"username": session['user']}, 
                                                            {"$pull" :
                                                                {"favourite_recipes" : remove_recipe}})
            flash('Removed from Favourites.')
            return redirect(url_for('profile', user=user['username'], recipe_id=recipe_id))
            
                                                        
    else:
        flash("You must be logged in to Edit, Save or Delete a recipe!")
        return redirect(url_for('get_recipes'))
        
    
    
# Login - taken and modified from Miroslav Svec's (username Miro) sessions from Slack DCD channel
@app.route('/login', methods=['GET'])
def login():
    # Check if user is not logged in already
    if 'user' in session:
        user_in_db = users.find_one({"username": session['user']})
        if user_in_db:
            # If so redirect user to his profile
            flash("You are logged in already!")
            return redirect(url_for('profile', user=user_in_db['username']))
    else:
        # Render the page for user to be able to log in
        return render_template("login.html")

# Check user login details from login form
# - taken and modified from Miroslav Svec's (username Miro) sessions from Slack DCD channel
@app.route('/user_auth', methods=['POST'])
def user_auth():
    form = request.form.to_dict()
    user_in_db = users.find_one({"username": form['username']})
    # Check for user in database
    if user_in_db:
        # If passwords match (hashed / real password)
        if check_password_hash(user_in_db['password'], form['user_password']):
            # Log user in (add to session)
            session['user'] = form['username']
            # If the user is admin redirect him to admin area
            if session['user'] == "admin":
                return redirect(url_for('admin'))
            else:
                flash("You were logged in!")
                return redirect(url_for('profile', user=user_in_db['username']))

        else:
            flash("Wrong password or user name!")
            return redirect(url_for('login'))
    else:
        flash("You must be registered!")
        return redirect(url_for('register'))

# Sign up - taken and modified from Miroslav Svec's (username Miro) sessions from Slack DCD channel
@app.route('/register', methods=['GET', 'POST'])
def register():
    # Check if user is not logged in already
    if 'user' in session:
        flash('You are already signed in!')
        return redirect(url_for('get_recipes'))
    if request.method == 'POST':
        form = request.form.to_dict()
        # Check if the password and password1 actually match
        if form['user_password'] == form['user_password1']:
            # If so try to find the user in db
            user = users.find_one({"username": form['username']})
            if user:
                flash("That username already exists!")
                return redirect(url_for('register'))
            # If user does not exist register new user
            else:
                # Hash password
                hash_pass = generate_password_hash(form['user_password'])
                # Create new user with hashed password
                users.insert_one(
                    {
                        'username': form['username'],
                        'email': form['email'],
                        'password': hash_pass,
                        'favourite_recipes': []
                    }
                )
                # Check if user is actually saved
                user_in_db = users.find_one(
                    {"username": form['username']})
                if user_in_db:
                    # Log user in (add to session)
                    session['user'] = user_in_db['username']
                    return redirect(url_for('profile', user=user_in_db['username']))
                else:
                    flash("There was a problem saving your profile")
                    return redirect(url_for('register'))

        else:
            flash("Passwords dont match!")
            return redirect(url_for('register'))

    return render_template("register.html")

# Log out- taken and modified from Miroslav Svec's (username Miro) sessions from Slack DCD channel
@app.route('/logout')
def logout():
    # Clear the session
    session.clear()
    flash('You were logged out!')
    return redirect(url_for('get_recipes'))
    
    
    
    
# Profile Page - taken and modified from Miroslav Svec's (username Miro) sessions from Slack DCD channel
@app.route('/profile/<user>')
def profile(user):
    # Check if user is logged in
    if 'user' in session:
        # If so get the user and pass him to template for now
        user_in_db = users.find_one({"username": user})
        favourites = mongo.db.users.find(user_in_db)
        
        return render_template('profile.html', user=user_in_db, favourites=favourites)
    else:
        flash("You must be logged in!")
        return redirect(url_for('get_recipes'))
        
        
# Admin area
@app.route('/admin')
def admin():
    if 'user' in session:
        
        
        
        if session['user'] == "admin":
            users = mongo.db.users.find()
            recipes = mongo.db.recipes.find()
            deleted = mongo.db.deleted.find()
            
            return render_template('admin.html', users=users, recipes=recipes, deleted=deleted)
        else:
            flash('Only Admins can access this page!')
            return redirect(url_for('get_recipes'))
    else:
        flash('You must be logged')
        return redirect(url_for('get_recipes'))
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True),