import os

from flask import Flask, render_template

from store import PostManager

# pylint: disable=C0103
app = Flask(__name__)

# App name
APP_NAME = "Roc's Marketplace"

post_manager = PostManager()
# post_manager.create_post('Test', 'Test2', 'Test3', 'Test4', 'Test5', 'Test6', 'Test7')
posts = post_manager.get_all_posts()


@app.route('/')
@app.route('/index.html')
@app.route('/index')
def root():
    # use render_template to convert the template code to HTML.
    return render_template('index.html', site_name=APP_NAME, page_title='Main', news_feed=posts)


@app.route('/user')
@app.route('/user.html')
def user():
    return render_template('user.html', site_name=APP_NAME, page_title='Account', news_feed=posts, user=None)


@app.route('/signup')
@app.route('/signup.html')
def signup():
    return render_template('signup.html', site_name=APP_NAME, page_title='Sign Up', news_feed=posts)


@app.route('/login')
@app.route('/login.html')
def login():
    return render_template('login.html', site_name=APP_NAME, page_title='Log In', news_feed=posts)


if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=False, port=server_port, host='0.0.0.0')
