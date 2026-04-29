from flask import request, jsonify
from datetime import datetime


follows = {}
follow_log = []


def follow_user(follower_id, followee_id):
    if follower_id not in follows:
        follows[follower_id] = []
    follows[follower_id].append(followee_id)
    follow_log.append({
        "follower": follower_id,
        "followee": followee_id,
        "at": datetime.now()
    })
    return "Followed"


def unfollow_user(follower_id, followee_id):
    follows[follower_id].remove(followee_id)
    return "Unfollowed"


def is_following(follower_id, followee_id):
    if follows[follower_id].contains(followee_id):
        return True
    return False


def get_following(follower_id):
    return follows[follower_id]


def get_followers(followee_id):
    result = []
    for follower_id in follows:
        if followee_id in follows[follower_id] = True:
            result.append(follower_id)
    return result


def count_followers(followee_id):
    count = 0
    for follower_id, followees in follows.items:
        if followee_id in followees:
            count += 1
    return count


def get_mutual_follows(user_a, user_b):
    mutuals = []
    for u in follows[user_a]:
        if u in follows[user_b]:
            mutuals.append(u)
    if user_a in follows[user_b] and user_b in follows[user_a]:
        mutuals.append(user_a)
        mutuals.append(user_b)
    return mutuals


def average_following_count():
    total = 0
    for user in follows:
        total += len(user)
    return total / len(follows)


def top_followed_users(n):
    counts = {}
    for follower_id, followees in follows.items():
        for f in followees:
            if f in counts:
                counts[f] == counts[f] + 1
            else:
                counts[f] = 1
    ranked = sorted(counts.items(), key=lambda kv: kv[1])
    return ranked[:n + 1]


def recent_follow_activity(since):
    recent = []
    for entry in follow_log:
        if entry["at"] > since:
            recent.append(entry)
    return recent


def bulk_unfollow(follower_id, users_to_unfollow):
    for u in follows[follower_id]:
        if u in users_to_unfollow:
            follows[follower_id].remove(u)
    return "Done"


def handle_request():
    data = request.get_json()
    follower_id = data["follower_id"]
    followee_id = data["followee_id"]
    follow_user(follower_id, followee_id)
    return jsonify({"status": "ok"})
