# import sqlite3
# from angry_site_flask.db_psql import db_session
# from angry_site_flask.model import User, Post
# 
# import pytest
# 
# 
# def test_get_close_db(app):
#     # with app.app_context():
#         # db = get_db()
#         # assert db is get_db()
# 
#     with pytest.raises(sqlite3.ProgrammingError) as e:
#         db.execute('SELECT 1')
#         # db_session.execute("SELECT 1")
# 
#     assert 'closed' in str(e.value)
