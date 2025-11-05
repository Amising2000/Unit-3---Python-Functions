# 1
# {"key_a": "value1", "key_b": 150, "key_d": 50}
# "key_c": False

# 2
120
60.0

# 3
def get_user_bio(user):
    bio = user.get('bio')
    if bio:
        return user['bio']
    else:
        return 'No bio avaliable'
print(get_user_bio({"username": "coder", "bio": "Python enthusiast"})) # "Python enthusiast"
print(get_user_bio({"username": "newbie"})) # "No bio available"

# 4
60
160

# 5
1

# 6
def get_total_engagement(post):
    if not post.get('likes'):
        post['likes'] = 0
    if not post.get('comments'):
        post['comments'] = 0
    if not post.get('shares'):
        post['shares'] = 0
    total = post['likes'] + post['comments'] + post['shares']
    return total
print(get_total_engagement({"likes": 100,"comments": 20,"shares": 10})) # 130
print(get_total_engagement({"likes": 50,"comments": 5})) # 55
print(get_total_engagement({"views": 1000})) # 0

# 7
3
3

# 8
{"key1": "value1", "key2": 200, "key3": 50}
{"key1": "value1", "key2": 200, "key4": True}

# 9
def find_most_followed(users):
    most_followers = 0
    top_user = ''
    for user in users:
        if user["followers"] > most_followers:
            most_followers = user['followers']
            top_user = user["username"]
    return top_user
users = [
    {"username": "alex", "followers": 1000},
    {"username": "sam", "followers": 5000},
    {"username": "jordan", "followers": 3000}
]
print(find_most_followed(users))