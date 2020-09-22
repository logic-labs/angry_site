from angry_site_flask.db_psql import db_session
from angry_site_flask.model import User, Post


def prfrm_test():
    values = {
        "test": "pbkdf2:sha256:50000$TCI4GzcX$0de171a4f4dac32e3364c7ddc7c14f3e2fa61f2d17574483f7ffbb431b4acb2f",
        "other": "pbkdf2:sha256:50000$kJPKsz6N$d2d4784f1b030a9761f5ccaeeaca413f27f2ecb76d6168407af962ddce849f79"
    }

    for uname, upasswd in values.items():
        # print("AAA!!!", uname, upasswd)
        if not db_session.query(User).filter(User.name==uname):
            user = User(name=uname, passwd=upasswd)
            db_session.add(user)
            db_session.commit()
    
    if not db_session.query(Post).filter(Post.title=="test title"):
        post = Post(title="test title", body="test test test test test test test test test test", author_id=1, created="2020-01-01 00:00:00");
        db_session.add(post)
        db_session.commit()
