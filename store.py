import datetime
import random
from google.cloud import datastore
# from google.cloud import storage

def get_client():
    return datastore.Client()

def generate_id():
    return random.randint(1,1000000000)


# Post obj, may need to move out of app.py

# Could maybe be simplified into author_username and current_username
# Then, we could just look in datastore for the necessary user information based on username
class Post:
    def __init__(self, post_id, username, display, description, image, profile, profile_image, comments, date=None):
        self.post_id = post_id
        self.username = username
        self.display = display
        self.description = description
        self.image = image
        self.profile_image = profile_image
        self.profile = profile
        self.comments = comments

        if date:
            self.date = date
        else:
            self.date = datetime.datatime.now()

# Base User obj
# Eventually user's will be loaded in through the DB?


class User:
    def __init__(self, username, name, photo_url, date=None):
        self.username = username
        self.name = name
        self.photo_url = photo_url

        if date:
            self.date = date
        else:
            self.date = datetime.datatime.now()


class Comment:
    def __init__(self, comment_id, post_id, username, comment, photo_url, date=None):
        self.comment_id = comment_id
        self.post_id = post_id
        self.username = username
        self.comment = comment
        self.photo_url = photo_url

        if date:
            self.date = date
        else:
            self.date = datetime.datatime.now()


class UserManager:
    def __init__(self):
        self.client = get_client()

    def create_user(self, username, name, photo_url):
        key = self.client.key("user")


class PostManager:
    def __init__(self):
        self.client = get_client()

    def create_post(self, username, display, description, image, profile, profile_url, comments):
        id = generate_id()
        post_id = self.client.key('post', id)

        post_entity = datastore.Entity(post_id)
        post_entity['post_id'] = id
        post_entity['username'] = username
        post_entity['display'] = display
        post_entity['description'] = description
        post_entity['image'] = image
        post_entity['profile'] = profile
        post_entity['profile_url'] = profile_url
        post_entity['comments'] = comments
        post_entity['date'] = datetime.datetime.now().strftime(
            '%Y%m%d %H:%M:%S')

        self.update_post(post_entity)

    # needs to be separate from create_post() for edit mode
    def update_post(self, entity):
        self.client.put(entity)
    
    def retrieve_post(self, id):
        key = self.client.key('post', int(id))
        return self.client.get(key)

    def delete_post(self, id):
        key = self.client.key('post', int(id))
        self.client.delete(key)


    def get_all_posts(self) -> list:
        posts = []
        query = self.client.query(kind='post')
        # self, post_id, username, display, description, image, profile, profile_image, comments, date=None
        for entity in query.fetch():
            post_id = entity['post_id']
            username = entity['username']
            display = entity['display']
            description = entity['description']
            image = entity['image']
            profile = entity['profile']
            profile_url = entity['profile_url']
            comments = entity['comments']
            date = entity['date']

            posts.append(Post(post_id, username, display, description,
                         image, profile, profile_url, comments, date))
        return posts

    def clear_all_posts(self):
        query = self.client.query(kind='post')
        for entity in query.fetch():
            self.client.delete(entity.key)

    # def save_file(self, _BUCKET_NAME, uploaded_file, c_type):
    #     gcs_client = storage.Client()
    #     storage_bucket = gcs_client.get_bucket(_BUCKET_NAME)
    #     blob = self.storage_bucket.blob(uploaded_file.filename)
    #     blob.upload_from_string(uploaded_file.read(), content_type=c_type)
    #     return blob.public_url