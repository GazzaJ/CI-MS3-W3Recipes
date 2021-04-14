import os
from flask import Flask, flash, render_template, redirect, \
    request, session, url_for, Response
from flask_pymongo import PyMongo
from better_profanity import profanity
from flask_sslify import SSLify
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, \
    check_password_hash
if os.path.exists('env.py'):
    import env

app = Flask(__name__)
sslify = SSLify(app, subdomains=True)

app.config['MONGO_DBNAME'] = os.environ.get('MONGO_DBNAME')
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.secret_key = os.environ.get('SECRET_KEY')

mongo = PyMongo(app)

response = Response()
response.headers['Strict-Transport-Security'] = \
    'max-age=31536000; includeSubDomains'
response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
response.headers['Cache-Control'] = 'no-cache, no-store, public, max-age=0'

# ----- Add custom profanities to the list

custom_badwords = ['arses', 'wankers']
profanity.add_censor_words(custom_badwords)


@app.route('/')
@app.route('/home')
def home():
    recipe = \
        mongo.db.recipes.find_one(
            {'_id': ObjectId('603799093d30368acbfdfdd0')})
    return render_template('index.html', recipe=recipe)


# ---------- Registration Form ----------

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # ----- Profanity Check -----
        # ----- Provided by better-profanity 0.7.0

        text = request.form.get('username').lower()
        clean_username = profanity.censor(text)

        # Checking if the username or email already exists

        existing_user = \
            mongo.db.users.find_one(
                {'username': request.form.get('username').lower()})

        if existing_user:
            flash('This username already exists!')
            return redirect(url_for('register'))

        register = {
            'username': clean_username,
            'password': generate_password_hash(
                request.form.get('password')),
            'city': '',
            'user_image': 'https://cdn.pixabay.com/photo/2015/10/05/22/37/'
                          'blank-profile-picture-973460_960_720.png',
            'subscribed': '',
            'email': '',
            'is_admin': False,
            }
        mongo.db.users.insert_one(register)

        # Place the new user into the session cookie

        session['user'] = request.form.get('username').lower()
        flash('Registration Successful')
        return redirect(url_for('profile', username=session['user']))
    return render_template('register.html')


# ---------- Login Page ----------

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        # Check if the username already exists in the DB

        existing_user = \
            mongo.db.users.find_one(
                {'username': request.form.get('username').lower()})

        if existing_user:

            # Ensure password matches the user input

            if check_password_hash(existing_user['password'],
                                   request.form.get('password')):
                session['user'] = request.form.get('username').lower()
                flash('Welcome to W3 Recipes, {}'.format(
                    request.form.get('username')))
                return redirect(url_for('get_recipes'))
            else:

                # Invalid password match

                flash('Username / Password incorrect!')
                return redirect(url_for('login'))
        else:

            # User doesn't exist

            flash('Username / Password incorrect!')
            return redirect(url_for('login'))

    return render_template('login.html')


# ---------- Profile Page ----------

@app.route('/profile/<username>', methods=['GET', 'POST'])
def profile(username):

    # Retrieve the session user's details from the DB

    username = mongo.db.users.find_one(
        {'username': session['user']})['username']
    city = mongo.db.users.find_one(
        {'username': session['user']})['city']
    email = mongo.db.users.find_one(
        {'username': session['user']})['email']
    image = mongo.db.users.find_one(
        {'username': session['user']})['user_image']
    subscribed = mongo.db.users.find_one(
        {'username': session['user']})['subscribed']

    if session['user']:
        return render_template(
            'profile.html',
            username=username,
            city=city,
            email=email,
            image=image,
            subscribed=subscribed,
            )

    return redirect(url_for('login'))


# ---------- Edit Profile ----------

@app.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    if request.method == 'POST':
        # ----- Profanity Check -----
        # ----- Provided by better-profanity 0.7.0

        clean_city = profanity.censor(request.form.get('city'))
        clean_email = profanity.censor(request.form.get('email'))

        # ----- Update specific DB fields only -----

        subscribed = request.form.get('subscribed')
        if subscribed is None:
            clean_email = ''
        mongo.db.users.update_one({'username': session['user']},
                                  {'$set': {
                                          'user_image': request.form.get(
                                              'user_image'),
                                          'city': clean_city,
                                          'subscribed': subscribed,
                                          'email': clean_email,
                                  }})

        flash('Profile Successfully Edited!')
        return redirect(url_for('profile', username=session['user']))

    # Retrieve the session user's details from the DB

    username = mongo.db.users.find_one(
        {'username': session['user']})['username']
    city = mongo.db.users.find_one(
        {'username': session['user']})['city']
    email = mongo.db.users.find_one(
        {'username': session['user']})['email']
    image = mongo.db.users.find_one(
        {'username': session['user']})['user_image']
    subscribed = mongo.db.users.find_one(
        {'username': session['user']})['subscribed']
    if session['user']:
        return render_template(
            'edit_profile.html',
            username=username,
            city=city,
            email=email,
            image=image,
            subscribed=subscribed,
            )


# ---------- MongoDB Collections ----------

recipe_coll = mongo.db.recipes
country_coll = mongo.db.countries
category_coll = mongo.db.recipe_category

# ---------- Items per Page ----------

per_page = 6


# ---------- Recipe Display Page ----------

@app.route('/get_recipes')
def get_recipes():
    # ----- Pagination adapted from -----
    # https://www.hacksparrow.com/databases/mongodb/pagination.html
    countries = country_coll.find().sort('name', 1)
    categories = category_coll.find()
    current_page = request.args.get('current_page', type=int, default=1)
    recipes = recipe_coll.find().sort('_id', -1).skip(
        per_page * (current_page - 1)).limit(per_page)
    total = recipe_coll.count()
    pages = range(1, int(round(total / per_page) + 1))
    last_page = max(range(1, int(round(total / per_page) + 1)))
    first_page = min(range(1, int(round(total / per_page) + 1)))
    prev_page = current_page - 1
    next_page = current_page + 1
    if session['user']:
        return render_template(
            'recipes.html',
            countries=countries,
            categories=categories,
            recipes=recipes,
            current_page=current_page,
            per_page=per_page,
            total=total,
            pages=pages,
            prev_page=prev_page,
            next_page=next_page,
            last_page=last_page,
            first_page=first_page
            )
    else:
        return redirect(url_for('home'))


# ---------- Recipe Text Search ----------

@app.route('/search', methods=['GET', 'POST'])
def search():

    # ----- Text Search -----

    text_search = request.form.get('text_search')
    recipes = recipe_coll.find({'$text': {'$search': text_search}})

    # ----- Pagination adapted from -----
    # https://www.hacksparrow.com/databases/mongodb/pagination.html

    current_page = request.args.get('current_page', type=int, default=1)
    total = recipe_coll.count()
    pages = range(1, int(round(total / per_page) + 1))
    last_page = max(range(1, int(round(total / per_page) + 1)))
    first_page = min(range(1, int(round(total / per_page) + 1)))
    prev_page = current_page - 1
    next_page = current_page + 1

    return render_template(
        'recipes.html',
        recipes=recipes,
        current_page=current_page,
        per_page=per_page,
        total=total,
        pages=pages,
        prev_page=prev_page,
        next_page=next_page,
        last_page=last_page,
        first_page=first_page
        )


# ---------- Recipe Filter by Country ----------

@app.route('/filter', methods=['GET', 'POST'])
def filter():

    # ----- Country Dropdown Filter -----

    countries = country_coll.find().sort('name', 1)
    country_filter = request.form.get('country_filter')
    recipes = recipe_coll.find({'$text': {'$search': country_filter}})

    # ----- Pagination adapted from -----
    # https://www.hacksparrow.com/databases/mongodb/pagination.html
    current_page = request.args.get('current_page', type=int, default=1)
    total = recipe_coll.count()
    pages = range(1, int(round(total / per_page) + 1))
    last_page = max(range(1, int(round(total / per_page) + 1)))
    first_page = min(range(1, int(round(total / per_page) + 1)))
    prev_page = current_page - 1
    next_page = current_page + 1

    return render_template(
        'recipes.html',
        recipes=recipes,
        countries=countries,
        current_page=current_page,
        per_page=per_page,
        total=total,
        pages=pages,
        prev_page=prev_page,
        next_page=next_page,
        last_page=last_page,
        first_page=first_page
        )


# ---------- Add a New Recipe ----------

@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
    if request.method == 'POST':
        # ----- Profanity Check -----
        # ----- Provided by better-profanity 0.7.0

        clean_ingred = profanity.censor(request.form.get('ingredients'))
        clean_method = profanity.censor(request.form.get('method'))
        clean_title = profanity.censor(request.form.get('title'))
        clean_prep = profanity.censor(request.form.get('prep_time'))
        clean_cook = profanity.censor(request.form.get('cooking_time'))
        clean_desc = profanity.censor(request.form.get('description'))

        # Find Country and retrieve flag code

        country = request.form.get('country_name')
        origin = country_coll.find_one({'name': country})['alpha2']

        # Format Recipe ingredients
        # https://stackoverflow.com/questions/1140958/
        # whats-a-quick-one-liner-to-remove-empty-lines-from-a-python-string
        text = "".join([s for s in clean_ingred.splitlines(
            True) if s.strip("\r\n")])
        ingred = text.rstrip()
        ingredients = ingred.split('\n')

        # Format Recipe steps
        text = "".join([s for s in clean_method.splitlines(
            True) if s.strip("\r\n")])
        meth = text.rstrip()
        method = meth.split('\n')

        recipe = {
            'country_name': country,
            'origin': origin,
            'title': clean_title,
            'recipe_type': request.form.get('recipe_category'),
            'vegan': request.form.get("vegan"),
            'vegetarian': request.form.get("vegetarian"),
            'image': request.form.get('image_url'),
            'prep_time': clean_prep,
            'cooking_time': clean_cook,
            'description': clean_desc,
            'servings': request.form.get('servings'),
            'ingredients': ingredients,
            'method': method,
            'uploaded_by': session['user'],
            }

        if recipe['image'] == '':
            recipe['image'] == 'https://pixy.org/src/13/thumbs350/135044.jpg'

        recipe_coll.insert_one(recipe)
        flash('Recipe Successfully Added!')
        return redirect(url_for('get_recipes'))
    if session['user']:
        countries = country_coll.find().sort('name', 1)
        categories = category_coll.find()
        return render_template('add_recipe.html', countries=countries,
                            categories=categories,
                            )
    else:
        return redirect(url_for('home'))


# ---------- Display Full Recipe ----------

@app.route('/full_recipe/<recipe_id>')
def full_recipe(recipe_id):
    recipe = recipe_coll.find_one({'_id': ObjectId(recipe_id)})
    origin = country_coll.find_one({'name': recipe['country_name']})
    flag = origin['alpha2']
    if session['user']:
        return render_template('full_recipe.html', recipe=recipe, flag=flag)
    else:
        return redirect(url_for('home'))


# ---------- Manage Recipes ----------
# -- Allows user to edit and delete a recipe --

@app.route('/manage_recipes', methods=['GET', 'POST'])
def manage_recipes():

    # Check if the user is Admin

    admin = mongo.db.users.find_one(
        {'username': session['user']})['is_admin']
    if admin is False:

        # Check how many recipes the user has uploaded

        recipes = recipe_coll.find({'uploaded_by': session['user']})
        uploaded = recipes.count()
        if uploaded == 0:
            flash('You have not uploaded any recipes yet!')
        if uploaded < per_page:
            return render_template('manage.html', recipes=recipes,
                                   uploaded=uploaded)
    else:
        current_page = request.args.get('current_page', type=int, default=1)
        recs = recipe_coll.find({'uploaded_by': session['user']})
        uploaded = recs.count()
        recipes = recipe_coll.find().sort('_id', -1).skip(
            per_page * (current_page - 1)).limit(per_page)
        total = recipe_coll.count()
        pages = range(1, int(round(total / per_page) + 1))
        last_page = max(range(1, int(round(total / per_page) + 1)))
        first_page = min(range(1, int(round(total / per_page) + 1)))
        prev_page = current_page - 1
        next_page = current_page + 1
        return render_template(
            'manage.html',
            recipes=recipes,
            admin=admin,
            current_page=current_page,
            per_page=per_page,
            total=total,
            pages=pages,
            prev_page=prev_page,
            uploaded=uploaded,
            next_page=next_page,
            last_page=last_page,
            first_page=first_page
            )


# ---------- Edit a Recipe ----------

@app.route('/edit_recipe/<recipe_id>', methods=['GET', 'POST'])
def edit_recipe(recipe_id):
    recipe = recipe_coll.find_one({'_id': ObjectId(recipe_id)})
    countries = country_coll.find().sort('name', 1)
    categories = category_coll.find()
    uploaded_by = recipe['uploaded_by']
    user = mongo.db.users.find_one({'username': session['user']})
    admin = user['is_admin']
    # ---------- POST the Edits to the DB ----------
    if request.method == 'POST':
        vegan = "on" if request.form.get("vegan") else "off"
        vegetarian = "on" if request.form.get("vegetarian") else "off"

        # ----- Profanity Check -----
        # ----- Provided by better-profanity 0.7.0

        clean_ingred = profanity.censor(request.form.get('ingredients'))
        clean_method = profanity.censor(request.form.get('method'))
        clean_title = profanity.censor(request.form.get('title'))
        clean_prep = profanity.censor(request.form.get('prep_time'))
        clean_cook = profanity.censor(request.form.get('cooking_time'))
        clean_desc = profanity.censor(request.form.get('description'))

        # Find Country and retrieve flag code

        country = request.form.get('country_name')
        origin = country_coll.find_one({'name': country})['alpha2']

        # Format Recipe ingredients
        # https://stackoverflow.com/questions/1140958/
        # whats-a-quick-one-liner-to-remove-empty-lines-from-a-python-string
        text = "".join([s for s in clean_ingred.splitlines(
            True) if s.strip("\r\n")])
        ingred = text.rstrip()
        ingredients = ingred.split('\n')

        # Format Recipe steps
        text = "".join([s for s in clean_method.splitlines(
            True) if s.strip("\r\n")])
        meth = text.rstrip()
        method = meth.split('\n')

        update = {
            'country_name': request.form.get('country_name'),
            'title': clean_title,
            'origin': origin,
            'recipe_type': request.form.get('recipe_category'),
            'vegan': vegan,
            'vegetarian': vegetarian,
            'image': request.form.get('image_url'),
            'prep_time': clean_prep,
            'cooking_time': clean_cook,
            'description': clean_desc,
            'servings': request.form.get('servings'),
            'ingredients': ingredients,
            'method': method,
            'uploaded_by': session['user'],
            }
        recipe_coll.update({'_id': ObjectId(recipe_id)}, update)
        flash('Recipe Successfully Edited!')
        return redirect(url_for('manage_recipes'))

    # ---------- Check if user "is_admin" ----------

    if admin is True:
        flash('')

        # ----- Check if session user uploaded the recipe -----

        return render_template('edit_recipe.html', recipe=recipe,
                               countries=countries,
                               uploaded_by=uploaded_by,
                               categories=categories)
    elif uploaded_by != session['user']:
        flash("You don't have the authority to edit this recipe!")
        return redirect(url_for('manage_recipes'))

    else:
        return render_template('edit_recipe.html', recipe=recipe,
                               countries=countries,
                               uploaded_by=uploaded_by,
                               categories=categories)


# ---------- Delete a Recipe ----------

@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    recipe = recipe_coll.find_one({'_id': ObjectId(recipe_id)})
    uploaded_by = recipe['uploaded_by']
    user = mongo.db.users.find_one({'username': session['user']})
    admin = user['is_admin']

    # ----- Check if session user uploaded the recipe -----

    if admin is True or uploaded_by == session['user']:
        recipe_coll.remove({'_id': ObjectId(recipe_id)})
        flash('Recipe Deleted Succesfully!')
        return redirect(url_for('manage_recipes'))

    else:
        flash("You don't have the authority to delete this recipe!")
        return redirect(url_for('manage_recipes'))


# ---------- Recipe Dashboard Page ----------

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


# ---------- Logout Page ----------

@app.route('/logout')
def logout():

    # Remove the user from the session cookies

    flash('You have been logged out')
    session.pop('user')
    return redirect(url_for('home'))


# ----- Error Handling Adapted from
# (https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/)

@app.errorhandler(400)
def bad_request(e):
    return (render_template('400.html'), 400)


@app.errorhandler(401)
def unauthorised(e):
    return (render_template('401.html'), 401)


@app.errorhandler(403)
def forbidden(e):
    return (render_template('403.html'), 403)


@app.errorhandler(404)
def not_found(e):
    return (render_template('404.html'), 404)


@app.errorhandler(405)
def method_not_allowed(e):
    return (render_template('405.html'), 405)


@app.errorhandler(500)
def server_error(e):
    return (render_template('500.html'), 500)


if __name__ == '__main__':
    app.run(
        host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=False)
    profanity.load_censor_words()
