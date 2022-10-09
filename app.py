import os

from flask import Flask, render_template

# pylint: disable=C0103
app = Flask(__name__)

# App name
APP_NAME = "CS1520 Project"

# Post obj, may need to move out of app.py


class Post:
    def __init__(self, display, username, date, description, image, profile, profile_image):
        self.display = display
        self.username = username
        self.date = date
        self.description = description
        self.image = image
        self.profile_image = profile_image
        self.profile = profile

# Base User obj


class User:
    posts = {}

    def __init__(self, name, creation_date):
        self.name = name
        self.date = creation_date


# Temporary list of posts
posts = {
    Post('John Martins', 'John Martins', 'Tue, Oct 4', 'Lorem ipsum.e..fe.af.a',
         'book.jpg', 'john_martins.jpeg', 'guillaume-bolduc-SGzbP-t1vlg-unsplash.jpg'),
    Post('John Martins', 'John Martins', 'Tue, Oct 4', 'Lorem ipsum.e..fe.af.a',
         'book.jpg', 'john_martins.jpeg', 'guillaume-bolduc-SGzbP-t1vlg-unsplash.jpg'),
    Post('John Martins', 'John Martins', 'Tue, Oct 4', 'Lorem ipsum.e..fe.af.a',
         'book.jpg', 'john_martins.jpeg', 'guillaume-bolduc-SGzbP-t1vlg-unsplash.jpg'),
    Post('John Martins', 'John Martins', 'Tue, Oct 4', 'Lorem ipsum.e..fe.af.a',
         'book.jpg', 'john_martins.jpeg', 'guillaume-bolduc-SGzbP-t1vlg-unsplash.jpg'),
    Post('John Martins', 'John Martins', 'Tue, Oct 4', 'Lorem ipsum.e..fe.af.a',
         'book.jpg', 'john_martins.jpeg', 'guillaume-bolduc-SGzbP-t1vlg-unsplash.jpg'),
    Post('John Martins', 'John Martins', 'Tue, Oct 4', 'Lorem ipsum.e..fe.af.a',
         'book.jpg', 'john_martins.jpeg', 'guillaume-bolduc-SGzbP-t1vlg-unsplash.jpg'),
    Post('John Martins', 'John Martins', 'Tue, Oct 4', 'Lorem ipsum.e..fe.af.a',
         'book.jpg', 'john_martins.jpeg', 'guillaume-bolduc-SGzbP-t1vlg-unsplash.jpg'),
    Post('John Martins', 'John Martins', 'Tue, Oct 4', 'Lorem ipsum.e..fe.af.a',
         'book.jpg', 'john_martins.jpeg', 'guillaume-bolduc-SGzbP-t1vlg-unsplash.jpg')
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
    return render_template('user.html', site_name=APP_NAME, page_title='Account', news_feed=posts)

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
