import datetime
import random
import logging 
from google.cloud import datastore

def get_client():
    return datastore.Client(project='rocsmarketplace')

def generate_id():
    return random.randint(1,1000000000)


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
            self.date = datetime.datetime.now().strftime('%Y%m%d %H:%M:%S')

# Base User obj
# Eventually user's will be loaded in through the DB?


class User:
    def __init__(self, username, name, email, photo_url, date=None):
        self.username = username
        self.name = name
        self.email = email
        self.photo_url = photo_url

        if date:
            self.date = date
        else:
            self.date = datetime.datetime.now().strftime('%Y%m%d %H:%M:%S')

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


_USER_ENTITY = 'User'

def _load_key(client, entity_type, entity_id=None, parent_key=None):
    # Load a datastore key using a particular client, and if known, the ID.
    # Note that the ID should be an int - we're allowing datastore to generate
    # them in this example.
    key = None
    if entity_id:
        key = client.key(entity_type, entity_id, parent=parent_key)
    else:
        # this will generate an ID
        key = client.key(entity_type)
    return key


# def _load_entity(client, entity_type, entity_id, parent_key=None):
#     # Load a datstore entity using a particular client, and the ID.

#     key = _load_key(client, entity_type, entity_id, parent_key)
#     entity = client.get(key)
#     logging.info('retrieved entity for %s' % (entity_id))
#     return entity



class UserManager:
    def __init__(self):
        self.client = get_client()

    # def create_user(self, username, name, photo_url):
    #     key = self.client.key("user")

    def load_user(self, username, passwordhash):
        # Load a user based on the passwordhash; if the passwordhash doesn't match
        # the username, then this should return None.

        client = get_client()
        q = client.query(kind=_USER_ENTITY)
        q.add_filter('username', '=', username)
        q.add_filter('passwordhash', '=', passwordhash)
        for user in q.fetch():
            return User(user['username'], user['email'])
        return None

    def save_user(self, user, passwordhash):
        """Save the user details to the datastore."""

        client = get_client()
        entity = datastore.Entity(_load_key(client, _USER_ENTITY, user.username))
        entity['username'] = user.username
        entity['email'] = user.email
        entity['passwordhash'] = passwordhash
        client.put(entity)



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
            comments = entity['comments']
            date = entity['date']

            posts.append(Post(post_id, username, display, description,
                         image, profile, profile_url, comments, date))
        return posts

    def clear_all_posts(self):
        query = self.client.query(kind='post')
        for entity in query.fetch():
            self.client.delete(entity.key)
