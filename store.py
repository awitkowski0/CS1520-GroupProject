from google.cloud import datastore


def get_client():
    return datastore.Client()


def test_client():
    client = get_client()
    key = client.key('new_type')
    return str(datastore.Entity(key))
