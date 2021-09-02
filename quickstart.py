from flask import Flask

app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return '<p>Hello World</p>'



# # HTML Escaping
# from markupsafe import escape

# @app.route("/<name>")
# def hello(name):
#     return f"Hello, {escape(name)}!"

# Routing
# @app.route('/')
# def index():
#     return 'Index Page'

# @app.route('/hello')
# def hello():
#     return 'Hello, World'


# Variable Rules
# You can add variable sections to a URL by marking sections with <variable_name>. Your function then receives the <variable_name> as a keyword argument. Optionally, you can use a converter to specify the type of the argument like <converter:variable_name>.

from markupsafe import escape

# @app.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     return f'User {escape(username)}'

# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return f'Post {post_id}'

# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     # show the subpath after /path/
#     return f'Subpath {escape(subpath)}'


# string  (default) accepts any text without a slash

# int accepts positive integers

# float   accepts positive floating point values

# path    like string but also accepts slashes

# uuid    accepts UUID strings



# Unique URLs / Redirection Behavior
# localhost:port/projects redirects to localhost:port/projects/ 
# but localhost:port/about/ doesn't redirect to localhost:port/about. Instead it gives a 404 error

# @app.route('/projects/')
# def projects():
#     return 'The project page'

# @app.route('/about')
# def about():
#     return 'The about page'



# URL Building
# URL Building
# To build a URL to a specific function, use the url_for() function. It accepts the name of the function as its first argument and any number of keyword arguments, each corresponding to a variable part of the URL rule. Unknown variable parts are appended to the URL as query parameters.

# Why would you want to build URLs using the URL reversing function url_for() instead of hard-coding them into your templates?

# Reversing is often more descriptive than hard-coding the URLs.

# You can change your URLs in one go instead of needing to remember to manually change hard-coded URLs.

# URL building handles escaping of special characters transparently.

# The generated paths are always absolute, avoiding unexpected behavior of relative paths in browsers.

# If your application is placed outside the URL root, for example, in /myapplication instead of /, url_for() properly handles that for you.


from flask import url_for

@app.route('/')
def index():
    return 'index'

# @app.route('/login')
# def login():
#     return 'login'

# HTTP Methods

def do_the_login():
    return 'do_the_login POST'

def show_the_login_form():
    return 'show_the_login_form GET'


from flask import request

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
    print(url_for('static', filename='style.css'))





