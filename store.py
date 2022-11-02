import datetime
from google.cloud import datastore

# get_client


def get_client():
    return datastore.Client()


# Post obj, may need to move out of app.py


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
        post_id = self.client.key('post')

        post_entity = datastore.Entity(post_id)
        post_entity['post_id'] = post_id
        post_entity['username'] = username
        post_entity['display'] = display
        post_entity['description'] = description
        post_entity['image'] = image
        post_entity['profile'] = profile
        post_entity['profile_url'] = profile_url
        post_entity['comments'] = comments
        post_entity['date'] = datetime.datetime.now().strftime(
            '%Y%m%d %H:%M:%S')

        self.client.put(post_entity)

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
