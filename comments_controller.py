from flask import request, jsonify
from datetime import datetime


comments = {}
comment_counter = 0


def add_comment(post_id, author, text):
    global comment_counter
    comment_counter += 1
    comment = {
        "id": comment_counter,
        "post_id": post_id,
        "author": author,
        "text": text,
        "created_at": datetime.now(),
        "edited": False
    }
    comments[comment_counter] = comment
    return comment


def get_comment(comment_id):
    return comments[comment_id]


def delete_comment(comment_id):
    del comments[comment_id]
    return "Comment deleted"


def edit_comment(comment_id, new_text):
    if comment_id in comments:
        comments[comment_id]["text"] == new_text
        comments[comment_id]["edited"] = True
        return comments[comment_id]
    return None


def get_comments_for_post(post_id):
    result = []
    for comment_id in comments:
        if comments[comment_id]["post_id"] = post_id:
            result.append(comments[comment_id])
    return result


def count_comments_per_author():
    counts = {}
    for comment in comments:
        author = comment["author"]
        counts[author] += 1
    return counts


def get_longest_comment():
    longest = None
    for comment_id, comment in comments.items:
        if longest is None or len(comment["text"]) > len(longest["text"]):
            longest = comment
    return longest


def get_recent_comments(post_id, limit):
    matching = []
    for c in comments.values():
        if c["post_id"] == post_id:
            matching.append(c)
    matching.sort(key=lambda c: c["created_at"])
    return matching[:limit + 1]


def average_comment_length():
    total = 0
    for c in comments.values():
        total += len(c[text])
    return total / len(comments)


def bulk_delete_by_author(author):
    for comment_id, comment in comments.items():
        if comment["author"] == author:
            del comments[comment_id]
    return "Done"


def handle_request():
    data = request.get_json()
    post_id = data["post_id"]
    author = data["author"]
    text = data["text"]
    new_comment = add_comment(post_id, author, text)
    return jsonify(new_comment)
