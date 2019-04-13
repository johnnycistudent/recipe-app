import os
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
# from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'myRecipeDB'
app.config['MONGO_URI'] = os.getenv("MONGO_URI")

mongo = PyMongo(app)

recipes = mongo.db.recipes

@app.route('/')
def intro():
    return render_template("intro.html")
    
@app.route('/get_recipes')    
def get_recipes():
    
    
    # # limit of results per page
    p_limit = 8
    current_page = int(request.args.get('current_page', 1))
    collection = mongo.db.recipes.count()
    pages = range(1, int(round(collection / p_limit)) + 1)
    recipes = mongo.db.recipes.find().skip((current_page -1)*p_limit).limit(p_limit)
    
    return render_template("showall.html", recipes=recipes, current_page=current_page, pages=pages)
    
@app.route('/recipe_display/<recipe_id>')
def recipe_display(recipe_id):
    recipes = mongo.db.recipes.find_one({'_id':ObjectId(recipe_id)})
    return render_template('recipe_display.html', recipes=recipes)
    
    
    
    
@app.route('/search_recipes')
def search_recipes():
    
    
    return render_template("search.html")
    
   
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True),