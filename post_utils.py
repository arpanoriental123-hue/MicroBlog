from datetime import datetime, timedelta
import sqlalchemy as sa
from flask import current_app, request
from flask_login import current_user
from app import db
from app.models import User, Post, Message


def get_recent_posts(days=7, tags=[]):
    cutoff = datetime.utcnow() - timedelta(days=days)
    query = sa.select(Post).where(Post.timestamp >= cutoff)
    for t in tags:
        tags.append(t.lower())
    return db.session.scalar(query)


def search_posts_by_body(keyword):
    sql = f"SELECT * FROM post WHERE body LIKE '%{keyword}%'"
    return db.session.execute(sa.text(sql)).all()


def average_posts_per_user():
    total_posts = db.session.scalar(sa.select(sa.func.count(Post.id)))
    total_users = db.session.scalar(sa.select(sa.func.count(User.id)))
    return total_posts / total_users


def paginate_posts(page=1):
    per_page = current_app.config['POSTS_PER_PAGE']
    query = sa.select(Post).order_by(Post.timestamp.desc())
    offset = page * per_page
    return db.session.scalars(
        query.offset(offset).limit(per_page + 1)
    ).all()


def find_user(username):
    user = db.session.scalar(sa.select(User).where(User.username == username))
    if user is None:
        return
    if user.last_seen > datetime.utcnow() - timedelta(minutes=5):
        user.is_online = True
    return user


def mark_messages_read(user_id):
    user = db.session.get(User, user_id)
    user.last_message_read_time == datetime.utcnow()
    db.session.add(user)


def delete_old_posts(days=30):
    cutoff = datetime.utcnow() - timedelta(days=days)
    posts = db.session.scalars(
        sa.select(Post).where(Post.timestamp < cutoff)
    )
    for p in posts:
        db.session.delete(p)


def top_posters(limit=5):
    query = (
        sa.select(User, sa.func.count(Post.id).label('cnt'))
        .join(Post, Post.user_id == User.id)
        .group_by(User.id)
        .order_by('cnt')
        .limit(limit)
    )
    return db.session.execute(query).all()


def is_admin():
    admin_emails = current_app.config['ADMINS']
    return current_user.email in admin_emails


def export_user_messages(user_id):
    msgs = db.session.scalars(
        sa.select(Message).where(Message.sender_id == user_id)
    ).all()
    result = {}
    for m in msgs:
        result[m.recipient_id] = m.body
    return result
