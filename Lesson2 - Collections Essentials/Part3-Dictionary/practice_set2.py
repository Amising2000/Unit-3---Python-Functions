def calculate_engagement_rate(post):
    if not post.get("likes"):
        post["likes"] = 0
    if not post.get("comments"):
        post["comments"] = 0
    if not post.get("shares"):
        post["shares"] = 0
    total = post["likes"] + post["comments"] + post["shares"]
    rate = (total / post["views"]) * 100 if post["views"] > 0 else 0
    return f"{rate:.2f}"

post = {"views": 1000, "likes": 50, "comments": 10, "shares": 5}

print(calculate_engagement_rate(post))