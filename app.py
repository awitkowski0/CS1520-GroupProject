import os
import datetime
import logging 
import flask
import store
import hashlib
from email.utils import parseaddr


# from flask import Flask, render_template, request
# from store import PostManager, Post, User, UserManager

# pylint: disable=C0103
app = flask.Flask(__name__)

# App name
APP_NAME = "Roc's Marketplace"

# Test current user
# Update this variable with the current user when login is successful
current_user = store.User('abc123', 'John Martins', 'abc123@pitt.edu', 'john_martins.jpeg')

post_manager = store.PostManager()
# post_manager.clear_all_posts()
# post_manager.create_post('Test', 'Test2', 'Test3', 'Test4', 'Test5', 'Test6', 'Test7')
# post_manager.create_post('abc123', 'title', 'stuff', '/static/assets/book.jpg', 'john_martins.jpeg', 'john_martins.jpeg', 'Test7')


@app.route('/')
@app.route('/index.html')
@app.route('/index')
def root():
    # use render_template to convert the template code to HTML.
    posts = post_manager.get_all_posts()
    return flask.render_template('index.html', site_name=APP_NAME, page_title='Main', news_feed=posts, user=current_user)

@app.route('/update', methods=['POST', 'GET'])
def update():
    mode = flask.request.values['mode']
    title = flask.request.values['title']
    description = flask.request.values['description']
    image = flask.request.values['file']

    if mode == 'create':
        # if you create a post, the profile image and the image next to the comment are the same
        post_manager.create_post(current_user.username, title, description, image, current_user.photo_url, current_user.photo_url, "")

    # mode == "edit"
    else:
        store.id = flask.request.values['id']
        entity = post_manager.retrieve_post(id)
        entity['display'] = title
        entity['description'] = description
        entity['image'] = image
        entity['date'] = datetime.datetime.now().strftime('%Y%m%d %H:%M:%S')
        post_manager.update_post(entity)

    return root()

@app.route('/delete')
def delete():
    store.id = flask.request.values['id']
    post_manager.delete_post(id)
    return root()


@app.route('/user')
@app.route('/user.html')
def user():
    posts = post_manager.get_all_posts()
    return flask.render_template('user.html', site_name=APP_NAME, page_title='Account', news_feed=posts, user=current_user)


@app.route('/signup')
@app.route('/signup.html')
def signup():
    return flask.render_template('signup.html', site_name=APP_NAME, page_title='Sign Up')


@app.route('/login')
@app.route('/login.html')
def login():
    return flask.render_template('login.html', site_name=APP_NAME, page_title='Log In')



@app.route('/dologin', methods=['POST'])
def dologin():
    username = flask.request.form.get('username')
    password = flask.request.form.get('password')
    passwordhash = get_password_hash(password)
    user = store.load_user(username, passwordhash)
    if user:
        flask.session['user'] = user.username
        return flask.redirect('/')
    # else:
    #     return show_login_page()

@app.route('/signout')
def signout():
    flask.session['user'] = None
    return flask.redirect('/')

@app.route('/register', methods=['POST'])
def register_user():
    username = flask.request.form.get('username')
    password1 = flask.request.form.get('password1')
    password2 = flask.request.form.get('password2')
    email = flask.request.form.get('email')
    errors = []
    if password1 != password2:
        errors.append('Passwords do not match.')
    email_parts = parseaddr(email)
    if len(email_parts) != 2 or not email_parts[1]:
        errors.append('Invalid email address: ' + str(email))

    user = store.User(username, email)
    if errors:
        # return show_page('/signup.html', 'Sign Up', errors=errors)
        return flask.render_template('login.html', site_name=APP_NAME, page_title='Log In')

    else:
        passwordhash = get_password_hash(password1)
        store.save_user(user, passwordhash)
        flask.session['user'] = user.username
        # return flask.redirect('/courses')
        return flask.render_template('user.html', site_name=APP_NAME, page_title='Account', news_feed=posts, user=current_user)


def get_password_hash(pw):
    encoded = pw.encode('utf-8')
    return hashlib.sha256(encoded).hexdigest()

# def show_login_page():
#     errors = ['You are not logged in.']
#     # return show_page('/login.html', 'Log In', errors)
#     return flask.render_template('signup.html', site_name=APP_NAME, page_title='Sign Up',)



@app.route('/createpost')
@app.route('/createpost.html')
def createpost():
    return flask.render_template('createpost.html', site_name=APP_NAME, page_title="Create Post")

@app.route('/editpost')
@app.route('/editpost.html')
def editpost():
    store.id = flask.request.values['id']
    entity = post_manager.retrieve_post(id)
    p = store.Post(
            entity['post_id'], 
            entity['username'], 
            entity['display'],
            entity['description'], 
            entity['image'], 
            entity['profile'], 
            entity['profile_url'], 
            entity['comments'], 
            entity['date']
        )
    return flask.render_template('editpost.html', site_name=APP_NAME, page_title='Edit Post', post=p)



if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=False, port=server_port, host='0.0.0.0')
