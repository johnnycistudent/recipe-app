import os
from flask import Flask, render_template, redirect, request, url_for, session, flash
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

@app.route('/')
def intro():
    return render_template("intro.html")
    
@app.route('/get_recipes')    
def get_recipes():
    
    
    # # Results per page
    p_limit = 9
    current_page = int(request.args.get('current_page', 1))
    collection = mongo.db.recipes.count()
    pages = range(1, int(round(collection / p_limit)) + 1)
    recipes = mongo.db.recipes.find().skip((current_page -1)*p_limit).limit(p_limit)
    
    return render_template("showall.html", recipes=recipes, current_page=current_page, pages=pages)
    
@app.route('/recipe_display/<recipe_id>')
def recipe_display(recipe_id):
    recipe = mongo.db.recipes.find_one({'_id':ObjectId(recipe_id)})
    return render_template('recipe_display.html', recipe=recipe)
    
    
    
    
@app.route('/search_recipes')
def search_recipes():
    
    
    return render_template("search.html")
    
    
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
                return redirect(url_for('get_recipes', user=user_in_db['username']))

        else:
            flash("Wrong password or user name!")
            return redirect(url_for('login'))
    else:
        flash("You must be registered!")
        return redirect(url_for('register'))

# Sign up
@app.route('/register', methods=['GET', 'POST'])
def register():
    # Check if user is not logged in already
    if 'user' in session:
        flash('You are already sign in!')
        return redirect(url_for('get_recipes'))
    if request.method == 'POST':
        form = request.form.to_dict()
        # Check if the password and password1 actualy match
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
                        'password': hash_pass
                    }
                )
                # Check if user is actualy saved
                user_in_db = users.find_one(
                    {"username": form['username']})
                if user_in_db:
                    # Log user in (add to session)
                    session['user'] = user_in_db['username']
                    return redirect(url_for('profile', user=user_in_db['username']))
                else:
                    flash("There was a problem savaing your profile")
                    return redirect(url_for('register'))

        else:
            flash("Passwords dont match!")
            return redirect(url_for('register'))

    return render_template("register.html")

# Log out
@app.route('/logout')
def logout():
    # Clear the session
    session.clear()
    flash('You were logged out!')
    return redirect(url_for('get_recipes'))
    
    
# Profile Page
@app.route('/profile/<user>')
def profile(user):
    # Check if user is logged in
    if 'user' in session:
        # If so get the user and pass him to template for now
        user_in_db = users.find_one({"username": user})
        return render_template('profile.html', user=user_in_db)
    else:
        flash("You must be logged in!")
        return redirect(url_for('get_recipes'))

# Admin area
@app.route('/admin')
def admin():
    if 'user' in session:
        if session['user'] == "admin":
            return render_template('admin.html')
        else:
            flash('Only Admins can access this page!')
            return redirect(url_for('get_recipes'))
    else:
        flash('You must be logged')
        return redirect(url_for('get_recipes'))
    

@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    all_categories = mongo.db.categories.find()
    return render_template('editrecipe.html', recipe=recipe, categories=all_categories)

 
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True),