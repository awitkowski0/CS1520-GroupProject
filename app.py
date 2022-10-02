import os

from flask import Flask, render_template

# pylint: disable=C0103
app = Flask(__name__)

# App name
APP_NAME = "CS1520 Project"

# Post obj, may need to move out of app.py


class Post:
    def __init__(self, name, date, body):
        self.display = name
        self.date = date
        self.body = body

# Base User obj


class User:
    posts = {}

    def __init__(self, name, creation_date):
        self.name = name
        self.date = creation_date


# Temporary list of posts
posts = {
    Post("Test Item", "01/01/2000", "Test body..."),
    Post("Test 4214", "01/01/2411", "Test body 2..."),
    Post("Test 241", "01/01/2141", "Test body 3..."),
    Post("Test 5125", "01/01/2141", "Test body 4..."),
    Post("Test 1234", "01/01/2241", "Test body 5..."),
    Post("Test 4211", "01/01/2141", "Test body 6..."),
    Post("Test 4219", "01/01/2141", "Test body 7..."),
    Post("Test 4219", "01/01/2141", "Test body 7..."),
    Post("Test 4219", "01/01/2141", "Test body 7..."),
    Post("Test 4219", "01/01/2141", "Test body 7..."),
    Post("Test 4219", "01/01/2141", "Test body 7...")
}


@app.route('/')
@app.route('/index.html')
@app.route('/index')
def root():
    # use render_template to convert the template code to HTML.
    return render_template('index.html', site_name=APP_NAME, page_title='Home', news_feed=posts)


@app.route('/user')
@app.route('/user.html')
def user():
    return render_template('user.html', site_name=APP_NAME, page_title='Account')


if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=False, port=server_port, host='0.0.0.0')
