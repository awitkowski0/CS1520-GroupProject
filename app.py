import os
import datetime

from flask import Flask, render_template

from store import PostManager, Post, User

# pylint: disable=C0103
app = Flask(__name__)

# App name
APP_NAME = "Roc's Marketplace"
_BUCKET_NAME = 'rocsmarketplace-image-uploads'

# Test current user
# Update this variable with the current user when login is successful
current_user = User('abc123', 'John Martins', 'john_martins.jpeg')

post_manager = PostManager()
# post_manager.clear_all_posts()
# post_manager.create_post('Test', 'Test2', 'Test3', 'Test4', 'Test5', 'Test6', 'Test7')
blank_post = Post("", "", "", "", "", "", "", "")


@app.route('/')
@app.route('/index.html')
@app.route('/index')
def root():
    # use render_template to convert the template code to HTML.
    posts = post_manager.get_all_posts()
    return render_template('index.html', site_name=APP_NAME, page_title='Main', news_feed=posts, user=current_user)

# @app.route('/create')
# def create():
#     return render_template('post.html', site_name=APP_NAME, page_title='Create Post', post=blank_post)

@app.route('/edit')
def edit():
    id = Flask.request.values['id']
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
    return render_template('post.html', site_name=APP_NAME, page_title='Edit Post', post=p)


@app.route('/update')
def update():
    mode = Flask.request.values['mode']
    title = Flask.request.values['title']
    description = Flask.request.values['description']
    image = Flask.request.values['file']

    # ---------- File uplaod code --- need to create GCS bucket first --------
    # file = Flask.request.files.get('file')
    # content_type = file.content_type
    # image = post_manager.save_file(_BUCKET_NAME, file, content_type)

    if mode == 'create':
        # if you create a post, the profile image and the image next to the comment are the same
        post_manager.create_post(current_user.name, title, description, image, current_user.photo_url, current_user.photo_url, [])

    # mode == "edit"
    else:
        id = Flask.request.values['id']
        entity = post_manager.retrieve_post(id)
        entity['display'] = title
        entity['description'] = description
        entity['image'] = image
        entity['date'] = datetime.datetime.now().strftime(
            '%Y%m%d %H:%M:%S')
        post_manager.update_post(entity)

    return root()

@app.route('/delete')
def delete():
    id = Flask.request.values['id']
    entity = post_manager.delete_post(id)




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


if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=False, port=server_port, host='0.0.0.0')
