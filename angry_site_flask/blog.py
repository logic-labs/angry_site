from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from angry_site_flask.auth import login_required
# from angry_site_flask.db import get_db
from angry_site_flask.db_psql import db_session
from angry_site_flask.model import User, Post
# from sqlalchemy import join, first
# from sqlalchemy import text

bp = Blueprint('blog', __name__)


@bp.route('/')
def index():
    # db = get_db()
    # posts = db.execute(
    #     'SELECT p.id, title, body, created, author_id, username'
    #     ' FROM post p JOIN user u ON p.author_id = u.id'
    #     ' ORDER BY created DESC'
    # ).fetchall()
    # posts = db_session.query(Post).join(User)
    posts = db_session.query(Post.id, Post.title, Post.body, Post.created, Post.author_id, User.name).join(User).order_by(Post.created)
    
    # flash(posts)
    
    return render_template('blog/index.html', posts=posts)


@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            # db = get_db()
            # db.execute(
            #     'INSERT INTO post (title, body, author_id)'
            #     ' VALUES (?, ?, ?)',
            #     (title, body, g.user['id'])
            # )
            # db.commit()
            uid = g.user["id"]
            post = Post(title=title, body=body, author_id=uid)
            db_session.add(post)
            db_session.commit()
            
            return redirect(url_for('blog.index'))

    return render_template('blog/create.html')
    

def get_post(id, check_author=True):
    # post = get_db().execute(
    #     'SELECT p.id, title, body, created, author_id, username'
    #     ' FROM post p JOIN user u ON p.author_id = u.id'
    #     ' WHERE p.id = ?',
    #     (id,)
    # ).fetchone()
    post = db_session.query(Post).join(User).filter(Post.id==id).first()

    if post is None:
        abort(404, "Post id {0} doesn't exist.".format(id))

    if check_author and post.author_id != g.user['id']:
        abort(403)

    return post
    

@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            # db = get_db()
            # db.execute(
            #     'UPDATE post SET title = ?, body = ?'
            #     ' WHERE id = ?',
            #     (title, body, id)
            # )
            # db.commit()
            post_to_upd = db_session.query(Post).filter(Post.id==id).first()
            post_to_upd.title = title
            post_to_upd.body = body
            db_session.commit()

            return redirect(url_for('blog.index'))

    return render_template('blog/update.html', post=post)


@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    # post = get_post(id)
    # db = get_db()
    # db.execute('DELETE FROM post WHERE id = ?', (id,))
    # db.commit()
    post_to_del = db_session.query(Post).filter(Post.id==id).first()
    db_session.delete(post_to_del)
    db_session.commit()

    return redirect(url_for('blog.index'))


# @bp.route('/create', methods=('GET', 'POST'))
# @login_required
# def create():
#     if request.method == 'POST':
#         title = request.form['title']
#         body = request.form['body']
#         error = None
# 
#         if not title:
#             error = 'Title is required.'
# 
#         if error is not None:
#             flash(error)
#         else:
#             db = get_db()
#             db.execute(
#                 'INSERT INTO post (title, body, author_id)'
#                 ' VALUES (?, ?, ?)',
#                 (title, body, g.user['id'])
#             )
#             db.commit()
#             return redirect(url_for('blog.index'))
# 
#     return render_template('blog/create.html')
# 
# 
# def get_post(id, check_author=True):
#     post = get_db().execute(
#         'SELECT p.id, title, body, created, author_id, username'
#         ' FROM post p JOIN user u ON p.author_id = u.id'
#         ' WHERE p.id = ?',
#         (id,)
#     ).fetchone()
# 
#     if post is None:
#         abort(404, "Post id {0} doesn't exist.".format(id))
# 
#     if check_author and post['author_id'] != g.user['id']:
#         abort(403)
# 
#     return post
# 
# 
# @bp.route('/<int:id>/update', methods=('GET', 'POST'))
# @login_required
# def update(id):
#     post = get_post(id)
# 
#     if request.method == 'POST':
#         title = request.form['title']
#         body = request.form['body']
#         error = None
# 
#         if not title:
#             error = 'Title is required.'
# 
#         if error is not None:
#             flash(error)
#         else:
#             db = get_db()
#             db.execute(
#                 'UPDATE post SET title = ?, body = ?'
#                 ' WHERE id = ?',
#                 (title, body, id)
#             )
#             db.commit()
#             return redirect(url_for('blog.index'))
# 
#     return render_template('blog/update.html', post=post)
# 
# 
# @bp.route('/<int:id>/delete', methods=('POST',))
# @login_required
# def delete(id):
#     post = get_post(id)
#     db = get_db()
#     db.execute('DELETE FROM post WHERE id = ?', (id,))
#     db.commit()
#     return redirect(url_for('blog.index'))
