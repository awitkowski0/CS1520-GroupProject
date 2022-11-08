import os
import datetime

from flask import Flask, render_template, request

from store import PostManager, Post, User

# pylint: disable=C0103
app = Flask(__name__)

# App name
APP_NAME = "Roc's Marketplace"
# _BUCKET_NAME = 'rocsmarketplace-image-uploads'

# Test current user
# Update this variable with the current user when login is successful
current_user = User('abc123', 'John Martins', 'john_martins.jpeg')

post_manager = PostManager()
# post_manager.clear_all_posts()
# post_manager.create_post('Test', 'Test2', 'Test3', 'Test4', 'Test5', 'Test6', 'Test7')
# post_manager.create_post('abc123', 'title', 'stuff', '/static/assets/book.jpg', 'john_martins.jpeg', 'john_martins.jpeg', 'Test7')


@app.route('/')
@app.route('/index.html')
@app.route('/index')
def root():
    # use render_template to convert the template code to HTML.
    posts = post_manager.get_all_posts()
    return render_template('index.html', site_name=APP_NAME, page_title='Main', news_feed=posts, user=current_user)

@app.route('/update', methods=['POST', 'GET'])
def update():
    mode = request.values['mode']
    title = request.values['title']
    description = request.values['description']
    image = request.values['file']

    if mode == 'create':
        # if you create a post, the profile image and the image next to the comment are the same
        post_manager.create_post(current_user.username, title, description, image, current_user.photo_url, current_user.photo_url, "")

    # mode == "edit"
    else:
        id = request.values['id']
        entity = post_manager.retrieve_post(id)
        entity['display'] = title
        entity['description'] = description
        entity['image'] = image
        entity['date'] = datetime.datetime.now().strftime('%Y%m%d %H:%M:%S')
        post_manager.update_post(entity)

    return root()

@app.route('/delete')
def delete():
    id = request.values['id']
    post_manager.delete_post(id)
    return root()


@app.route('/user')
@app.route('/user.html')
def user():
    posts = post_manager.get_all_posts()
    return render_template('user.html', site_name=APP_NAME, page_title='Account', news_feed=posts, user=current_user)


@app.route('/signup')
@app.route('/signup.html')
def signup():
    return render_template('signup.html', site_name=APP_NAME, page_title='Sign Up')


@app.route('/login')
@app.route('/login.html')
def login():
    return render_template('login.html', site_name=APP_NAME, page_title='Log In')

@app.route('/createpost')
@app.route('/createpost.html')
def createpost():
    return render_template('createpost.html', site_name=APP_NAME, page_title="Create Post")

@app.route('/editpost')
@app.route('/editpost.html')
def editpost():
    id = request.values['id']
    entity = post_manager.retrieve_post(id)
    p = Post(
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
    return render_template('editpost.html', site_name=APP_NAME, page_title='Edit Post', post=p)



if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=False, port=server_port, host='0.0.0.0')
