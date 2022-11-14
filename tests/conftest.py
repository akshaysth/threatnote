import os

import pytest

from threatnote import create_app
from threatnote.models import Organization, User, db

with open(os.path.join(os.path.dirname(__file__), "data.sql"), "rb") as f:
    _data_sql = f.read().decode("utf8")


@pytest.fixture(scope="module")
def app():
    app = create_app()
    app.config.from_object("config.TestingConfig")

    with app.test_client() as app_client:
        with app.app_context():
            yield app_client


@pytest.fixture(scope="module")
def init_database(app):
    db.create_all()

    org = Organization("testing", "test", 2)

    user1 = User(
        name="admin",
        email="admin1@test.io",
        password_plaintext="admin",
        role="admin",
        org_id=1,
    )
    user2 = User(
        name="user",
        email="user1@test.io",
        password_plaintext="user",
        org_id=2,
    )

    db.session.add(org)
    db.session.add(user1)
    db.session.add(user2)

    db.session.commit()

    yield

    db.drop_all()


@pytest.fixture(scope="module")
def new_admin_user():
    user = User(
        "admin",
        "admin@note.io",
        "admin",
        2,
        "admin",
    )
    return user


@pytest.fixture(scope="module")
def new_user():
    user = User(
        "user",
        "user@note.io",
        "user",
        2,
    )
    return user


@pytest.fixture(scope="function")
def login_default_user(app):
    app.post(
        "/login",
        data=dict(email="admin1@test.io", password="admin"),
        follow_redirects=True,
    )
    yield

    app.get("/logout", follow_redirects=True)


