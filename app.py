import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
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
            flash("This username already exists!")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # Place the new user into the session cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful")
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
                    request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))

            else:
                # Invalid password match
                flash("Username / Password incorrect, please try again!")
                return redirect(url_for("login"))

        else:
            # User doesn't exist
            flash("Username / Password incorrect, please try again")
            return redirect(url_for("login"))

    return render_template("login.html")


# ---------- Profile Page ----------
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # Retrieve the session user's username from the DB
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    return render_template("profile.html", username=username)

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


# ---------- Recipe Display Page ----------
@app.route("/get_recipes")
def get_recipes():
    recipes = mongo.db.recipes.find()
    return render_template("recipes.html", recipes=recipes)


# ---------- Add a New Recipe ----------
@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        ingredients = request.form.get("ingredients")
        ingredients = ingredients.split('\n')
        method = request.form.get("method")
        method = method.split('\n')
        recipe = {
            "country_name": request.form.get("country_name"),
            "title": request.form.get("title"),
            "image": request.form.get("image_url"),
            "description": request.form.get("description"),
            "servings": request.form.get("servings"),
            "ingredients": ingredients,
            "method": method,
            "uploaded_by": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Successfully Added!")
        return redirect(url_for("get_recipes"))

    countries = mongo.db.countries.find()
    return render_template(
        "add_recipe.html", countries=countries)


# ---------- Display Full Recipe ----------
@app.route("/full_recipe/<recipe_id>")
def full_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})    
    return render_template("full_recipe.html", recipe=recipe)


# ---------- Manage Recipes ----------
# -- Allows user to edit and delete a recipe --
@app.route("/manage_recipes", methods=["GET", "POST"])
def manage_recipes():    
    recipes = mongo.db.recipes.find()       
    return render_template("manage.html", recipes=recipes,)


# ---------- Edit a Recipe ----------
@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    countries = mongo.db.countries.find()
    return render_template("edit_recipe.html", recipe=recipe, countries=countries)


# ---------- Logout Page ----------
@app.route("/logout")
def logout():
    # Remove the user from the session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
