import datetime
import random
from google.cloud import datastore

def get_client():
    return datastore.Client(project='rocsmarketplace')

def generate_id():
    return random.randint(1,1000000000)


# Post obj, may need to move out of app.py

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
            self.date = datetime.datetime.now().strftime('%Y%m%d %H:%M:%S')

class Post:
    def __init__(self, post_id, username, display, description, image, profile, profile_image, comments: list, date=None):
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
            self.date = datetime.datetime.now().strftime('%Y%m%d %H:%M:%S')
    def add_comment(self, comment: Comment):
        self.comments.append(comment)

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
            self.date = datetime.datetime.now().strftime('%Y%m%d %H:%M:%S')


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

        for entity in query.fetch():
            post_id = entity['post_id']
            username = entity['username']
            display = entity['display']
            description = entity['description']
            image = entity['image']
            profile = entity['profile']
            profile_url = entity['profile_url']
            date = entity['date']

            posts.append(Post(post_id, username, display, description,
                         image, profile, profile_url, self.get_all_comments(post_id), date))
        return posts

    def clear_all_posts(self):
        query = self.client.query(kind='post')
        for entity in query.fetch():
            self.client.delete(entity.key)

    def get_all_comments(self, post_id) -> list:
        posts = self.get_all_posts(self)
        comments = []

        for post in posts:
            if (post.post_id == post_id):
                return post.comments
        return comments


"""
Comment manager will store comments for each post
"""
class CommentManager:
    def __init__(self):
        self.client = get_client()

    def create_comment(self, username, comment, profile_url):
        id = generate_id()
        post_id = self.client.key('comment', id)

        post_entity = datastore.Entity(post_id)
        post_entity['comment_id'] = id
        post_entity['username'] = username
        post_entity['comment'] = comment
        post_entity['profile_url'] = profile_url
        post_entity['date'] = datetime.datetime.now().strftime(
            '%Y%m%d %H:%M:%S')

        self.update_comment(post_entity)

    def update_comment(self, entity):
        self.client.put(entity)

    def retrieve_comment(self, id):
        key = self.client.key('comment', int(id))
        return self.client.get(key)

    def delete_comment(self, id):
        key = self.client.key('comment', int(id))
        self.client.delete(key)

    def get_all_posts(self) -> list:
        posts = []
        query = self.client.query(kind='comment')

        for entity in query.fetch():
            comment_id = entity['comment_id']
            username = entity['username']
            comment = entity['comment']
            profile = entity['profile']
            profile_url = entity['profile_url']
            date = entity['date']

            posts.append(Comment(comment_id, username, comment,
                                 profile, profile_url, date))

        return posts