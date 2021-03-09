import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from flask_paginate import Pagination,get_page_parameter
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


# ---------- Registration Form ----------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Checking if the username or email already exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("This username already exists!", "one")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "city": "",
            "user_image": "https://cdn.pixabay.com/photo/2015/10/05/22/37/" +
            "blank-profile-picture-973460_960_720.png",
            "subscribed": False,
            "email": "",
            "is_admin": False
        }
        mongo.db.users.insert_one(register)

        # Place the new user into the session cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful", "two")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


# ---------- Login Page ----------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Check if the username already exists in the DB
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # Ensure password matches the user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome to W3 Recipes, {}".format(
                    request.form.get("username")), "three")
                return redirect(url_for("get_recipes"))

            else:
                # Invalid password match
                flash("Username / Password incorrect!")
                return redirect(url_for("login"))

        else:
            # User doesn't exist
            flash("Username / Password incorrect!")
            return redirect(url_for("login"))

    return render_template("login.html")


# ---------- Profile Page ----------
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # Retrieve the session user's details from the DB
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    city = mongo.db.users.find_one(
        {"username": session["user"]})["city"]
    email = mongo.db.users.find_one(
        {"username": session["user"]})["email"]
    image = mongo.db.users.find_one(
        {"username": session["user"]})["user_image"]
    subscribed = mongo.db.users.find_one(
        {"username": session["user"]})["subscribed"]
    if session["user"]:
        return render_template("profile.html",
        username=username, city=city, email=email,
        image=image, subscribed=subscribed)

    return redirect(url_for("login"))


# ---------- Edit Profile ----------
@app.route("/edit_profile/<username>", methods=["GET", "POST"])
def edit_profile(username):
    # Retrieve the session user's details from the DB
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    city = mongo.db.users.find_one(
        {"username": session["user"]})["city"]
    email = mongo.db.users.find_one(
        {"username": session["user"]})["email"]
    image = mongo.db.users.find_one(
        {"username": session["user"]})["user_image"]
    subscribed = mongo.db.users.find_one(
        {"username": session["user"]})["subscribed"]
    if session["user"]:
        return render_template("edit_profile.html",
        username=username, city=city, email=email,
        image=image, subscribed=subscribed)


# ---------- MongoDB Collections ----------
recipe_coll = mongo.db.recipes
country_coll = mongo.db.countries
per_page = 6


# ---------- Recipe Display Page ----------
@app.route("/get_recipes")
def get_recipes():
    # ----- Pagination adapted from https://pythonhosted.org/Flask-paginate/
    current_page = request.args.get('current_page', type=int, default=1)
    offset = (current_page - 1) * per_page
    recipes = recipe_coll.find().sort('_id', -1).skip(
        offset).limit(per_page)
    total = recipes.count()
    pages = range(1, int(round(total / per_page + 1)))
    prev_page = current_page - 1
    next_page = current_page + 1
    countries = country_coll.find().sort("country", 1)
    return render_template("recipes.html",
        recipes=recipes, countries=countries,
        current_page=current_page, pages=pages,
        total=total, per_page=per_page, prev_page=prev_page,
        next_page=next_page)


# ---------- Recipe Text Search ----------
@app.route("/search", methods=["GET", "POST"])
def search():
    current_page = request.args.get('current_page', type=int, default=1)
    offset = (current_page - 1) * per_page
    text_search = request.form.get("text_search")
    recipes = recipe_coll.find(
        {"$text": {"$search": text_search}}).skip(
        offset).limit(per_page)
    total = recipes.count()
    pages = range(1, int(round(total / per_page)) + 1)
    prev_page = current_page - 1
    next_page = current_page + 1
    return render_template("recipes.html",
        recipes=recipes, current_page=current_page, pages=pages,
        total=total, per_page=per_page, prev_page=prev_page,
        next_page=next_page)


# ---------- Recipe Filter by Country ----------
@app.route("/filter", methods=["GET", "POST"])
def filter():
    current_page = request.args.get('current_page', type=int, default=1)
    offset = (current_page - 1) * per_page
    country_filter = request.form.get("country_filter")
    recipes = recipe_coll.find(
        {"$text": {"$search": country_filter}}).skip(
        offset).limit(per_page)
    total = recipes.count()
    pages = range(1, int(round(total / per_page)) + 1)
    prev_page = current_page - 1
    next_page = current_page + 1
    return render_template("recipes.html",
        recipes=recipes, current_page=current_page, pages=pages,
        total=total, per_page=per_page, prev_page=prev_page,
        next_page=next_page)


# ---------- Add a New Recipe ----------
@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        # Get and format Recipe ingredients and steps
        ingredients = request.form.get("ingredients")
        ingredients = ingredients.split('\n')
        method = request.form.get("method")
        method = method.split('\n')
        recipe = {
            "country_name": request.form.get("country_name"),
            "title": request.form.get("title"),
            "image": request.form.get("image_url"),
            "prep_time": request.form.get("prep_time"),
            "cooking_time": request.form.get("cooking_time"),
            "description": request.form.get("description"),
            "servings": request.form.get("servings"),
            "ingredients": ingredients,
            "method": method,
            "uploaded_by": session["user"]
        }
        recipe_coll.insert_one(recipe)
        flash("Recipe Successfully Added!", "five")
        return redirect(url_for("get_recipes"))

    countries = country_coll.find().sort("country", 1)
    return render_template(
        "add_recipe.html", countries=countries)


# ---------- Display Full Recipe ----------
@app.route("/full_recipe/<recipe_id>")
def full_recipe(recipe_id):
    recipe = recipe_coll.find_one({"_id": ObjectId(recipe_id)})
    return render_template("full_recipe.html", recipe=recipe)


# ---------- Manage Recipes ----------
# -- Allows user to edit and delete a recipe --
@app.route("/manage_recipes", methods=["GET", "POST"])
def manage_recipes():
    # Check if the user is Admin
    admin = mongo.db.users.find_one(
        {"username": session["user"]})["is_admin"]
    # Recipe search and pagination
    current_page = request.args.get('current_page', type=int, default=1)
    offset = (current_page - 1) * per_page
    recipes = recipe_coll.find().sort('_id', 1).skip(
        offset).limit(per_page)
    total = recipes.count()
    pages = range(1, int(round(total / per_page)) + 1)
    prev_page = current_page - 1
    next_page = current_page + 1
    # Check how many recipes the user has uploaded
    uploaded = recipe_coll.count(
        {"uploaded_by": session["user"]})
    if uploaded == 0:
        flash("You have not uploaded any recipes yet!", "six")
    return render_template("manage.html", recipes=recipes,
        current_page=current_page, pages=pages,total=total,
        per_page=per_page, admin=admin, uploaded=uploaded,
        prev_page=prev_page, next_page=next_page)


# ---------- Edit a Recipe ----------
@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        # Get and format Recipe ingredients and steps
        ingredients = request.form.get("ingredients")
        ingredients = ingredients.split('\n')
        method = request.form.get("method")
        method = method.split('\n')
        update = {
            "country_name": request.form.get("country_name"),
            "title": request.form.get("title"),
            "image": request.form.get("image_url"),
            "prep_time": request.form.get("prep_time"),
            "cooking_time": request.form.get("cooking_time"),
            "description": request.form.get("description"),
            "servings": request.form.get("servings"),
            "ingredients": ingredients,
            "method": method,
            "uploaded_by": session["user"]
        }
        recipe_coll.update({"_id": ObjectId(recipe_id)}, update)
        flash("Recipe Successfully Edited!", "seven")
        return redirect(url_for("manage_recipes"))

    recipe = recipe_coll.find_one({"_id": ObjectId(recipe_id)})
    countries = country_coll.find().sort("country", 1)
    return render_template(
        "edit_recipe.html", recipe=recipe, countries=countries)


# ---------- Delete a Recipe ----------
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    recipe_coll.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Deleted Succesfully!")
    return redirect(url_for("manage_recipes"))


# ---------- Recipe Dashboard Page ----------
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# ---------- Logout Page ----------
@app.route("/logout")
def logout():
    # Remove the user from the session cookies
    flash("You have been logged out", "eight")
    session.pop("user")
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
