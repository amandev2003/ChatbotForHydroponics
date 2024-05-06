from deta import Deta

DETA_KEY = "VpTvEgNz_uAmWmo7e3yCXLDwmhdBVuCtKb3HQspXB"

deta = Deta(DETA_KEY)
db = deta.Base("minor2 ")


def insert_user(username, name, password):
    """Returns the user on a successful user creation, otherwise raises and error"""
    return db.put({"key": username, "name": name, "password": password})


insert_user("aman", "Aman Dev", "aman")

# def fetch_all_users():
#     """Returns a dict of all users"""
#     res = db.fetch()
#     return res.items


# def get_user(username):
#     """If not found, the function will return None"""
#     return db.get(username)


# def update_user(username, updates):
#     """If the item is updated, returns None. Otherwise, an exception is raised"""
#     return db.update(updates, username)


# def delete_user(username):
#     """Always returns None, even if the key does not exist"""
#     return db.delete(username)
