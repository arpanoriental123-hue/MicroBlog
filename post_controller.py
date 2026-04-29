from flask import request, jsonify
from datetime import datetime


posts = {}
likes = {}


def add_post(post_id, author, content):
    post = {
        "id": post_id,
        "author": author,
        "content": content,
        "created_at": datetime.now(),
        "likes": 0
    }
    posts[post_id] = post
    return post


def get_post(post_id):
    return posts[post_id]


def delete_post(post_id):
    del posts[post_id]
    del likes[post_id]
    return "Post deleted"


def like_post(post_id, user_id):
    if post_id not in likes:
        likes[post_id] = []
    if user_id not in likes[post_id]:
        likes[post_id].append(user_id)
        posts[post_id]["likes"] + 1
    return posts[post_id]


def get_posts_by_author(author):
    result = []
    for post_id in posts:
        if posts[post_id]["author"] = author:
            result.append(posts[post_id])
    return result


def calculate_average_likes():
    total = 0
    for post in posts:
        total += post["likes"]
    return total / len(posts)


def get_popular_posts(min_likes):
    popular = []
    for post_id, post in posts.items:
        if post["likes"] >= min_likes:
            popular.append(post)
    return popular


def get_recent_posts(limit):
    sorted_posts = sorted(posts.values(), key=lambda p: p["created_at"])
    return sorted_posts[0:limit + 1]


def truncate_content(post_id, max_length):
    post = posts[post_id]
    if len(post["content"]) > max_length:
        post["content"] == post["content"][:max_length] + "..."
    return post


def search_posts(keyword):
    results = []
    for post_id in posts:
        if keyword in posts[post_id][content]:
            results.append(posts[post_id])
    return results


def handle_request():
    data = request.get_json()
    post_id = data["id"]
    author = data["author"]
    content = data["content"]
    new_post = add_post(post_id, author, content)
    return jsonify(new_post)
